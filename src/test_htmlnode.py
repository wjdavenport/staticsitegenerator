import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_with_props(self):
        # Create an HTMLNode with tag, value, children, and props
        node = HTMLNode(tag='div', value='Hello, World!', children=[], props={'class': 'container'})

        # Verify that to_html returns the expected HTML string
        expected_html = '<div class="container">Hello, World!</div>'
        self.assertEqual(node.to_html(), expected_html)


    def test_props_to_html_without_props(self):
        # Create an HTMLNode without any props
        node = HTMLNode(tag='p', value='Lorem ipsum', children=[])

        # Verify that props_to_html returns an empty string
        expected_html = ''
        self.assertEqual(node.props_to_html(), expected_html)

    # def test_to_html_with_children(self):
    #     # Create an HTMLNode with tag, value, children, and props
    #     node = HTMLNode(tag='div', value='Hello, World!', children=[
    #         HTMLNode(tag='p', value='Lorem ipsum', children=[]),
    #         HTMLNode(tag='span', value='Dolor sit amet', children=[]),
    #     ], props={'class': 'container'})
    #     # Verify that to_html returns the expected HTML string
    #     expected_html = '<div class="container">\n  <p>Lorem ipsum</p>\n  <span>Dolor sit amet</span>\n</div>'
    #     self.assertEqual(node.to_html(), expected_html)

    def test_to_html_without_children(self):
        # Create an HTMLNode without any children
        node = HTMLNode(tag='div', value='Hello, World!', children=[], props={'class': 'container'})
        # Verify that to_html returns the expected HTML string
        expected_html = '<div class="container">Hello, World!</div>'
        self.assertEqual(node.to_html(), expected_html)

    def test_repr(self):
        # Create an HTMLNode with tag, value, children, and props
        node = HTMLNode(tag='div', value='Hello, World!', children=[], props={'class': 'container'})
        # Verify that the __repr__ method returns the expected string representation
        expected_repr = "HTMLNode(tag='div', value='Hello, World!', children=[], props={'class': 'container'})"
        self.assertEqual(repr(node), expected_repr)

if __name__ == '__main__':
    unittest.main()