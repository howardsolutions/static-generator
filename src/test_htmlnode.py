import unittest
from htmlnode import HTMLNode, LeafNode

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

if __name__ == "__main__":
    unittest.main() 