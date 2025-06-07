import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "Click me!",
            None,
            {"href": "https://www.google.com", "target": "_blank"}
        )
        expected = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_empty(self):
        node = HTMLNode("p", "Hello world")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_numbers(self):
        node = HTMLNode(
            "div",
            None,
            None,
            {"width": 100, "height": 200, "class": "container"}
        )
        expected = 'width=100 height=200 class="container"'
        self.assertEqual(node.props_to_html(), expected)

    def test_repr(self):
        node = HTMLNode(
            "p",
            "Hello world",
            None,
            {"class": "text"}
        )
        expected = 'HTMLNode(p, Hello world, None, {"class": "text"})'
        self.assertEqual(repr(node), expected)

    def test_to_html_not_implemented(self):
        node = HTMLNode("p", "Hello world")
        with self.assertRaises(NotImplementedError):
            node.to_html()

class TestLeafNode(unittest.TestCase):
    def test_leaf_node_with_tag_and_value(self):
        node = LeafNode("p", "Hello world")
        expected = "<p>Hello world</p>"
        self.assertEqual(node.to_html(), expected)

    def test_leaf_node_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected)
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_node_without_tag(self):
        node = LeafNode(value="Hello world")
        expected = "Hello world"
        self.assertEqual(node.to_html(), expected)

    def test_leaf_node_missing_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p")

    def test_leaf_node_repr(self):
        node = LeafNode("p", "Hello world", {"class": "text"})
        expected = 'HTMLNode(p, Hello world, None, {"class": "text"})'
        self.assertEqual(repr(node), expected)

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("p", "First child")
        child2 = LeafNode("p", "Second child")
        child3 = LeafNode("p", "Third child")
        parent_node = ParentNode("div", [child1, child2, child3])
        expected = "<div><p>First child</p><p>Second child</p><p>Third child</p></div>"
        self.assertEqual(parent_node.to_html(), expected)

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container", "id": "main"})
        expected = '<div class="container" id="main"><span>child</span></div>'
        self.assertEqual(parent_node.to_html(), expected)

    def test_to_html_with_empty_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_with_nested_structure(self):
        # Create a complex nested structure
        leaf1 = LeafNode("b", "bold")
        leaf2 = LeafNode("i", "italic")
        leaf3 = LeafNode("u", "underline")
        
        inner_div = ParentNode("div", [leaf1, leaf2])
        outer_div = ParentNode("div", [inner_div, leaf3])
        
        expected = "<div><div><b>bold</b><i>italic</i></div><u>underline</u></div>"
        self.assertEqual(outer_div.to_html(), expected)

    def test_to_html_with_mixed_content(self):
        # Test mixing text nodes with element nodes
        text_node = LeafNode(value="Some text")
        bold_node = LeafNode("b", "bold text")
        parent_node = ParentNode("div", [text_node, bold_node])
        expected = "<div>Some text<b>bold text</b></div>"
        self.assertEqual(parent_node.to_html(), expected)

    def test_to_html_with_deep_nesting(self):
        # Test very deep nesting
        current = LeafNode("span", "deepest")
        for i in range(5):
            current = ParentNode("div", [current])
        expected = "<div><div><div><div><div><span>deepest</span></div></div></div></div></div>"
        self.assertEqual(current.to_html(), expected)

    def test_to_html_with_complex_props(self):
        child = LeafNode("span", "child")
        parent = ParentNode("div", [child], {
            "class": "container",
            "data-test": "value",
            "style": "color: red;",
            "onclick": "alert('click')"
        })
        expected = '<div class="container" data-test="value" style="color: red;" onclick="alert(\'click\')"><span>child</span></div>'
        self.assertEqual(parent.to_html(), expected)

    def test_to_html_with_invalid_inputs(self):
        # Test with None tag
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("span", "child")])

        # Test with None children
        with self.assertRaises(ValueError):
            ParentNode("div", None)

        # Test with invalid children type
        with self.assertRaises(AttributeError):
            ParentNode("div", ["not a node"])

if __name__ == "__main__":
    unittest.main() 