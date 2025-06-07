import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main() 