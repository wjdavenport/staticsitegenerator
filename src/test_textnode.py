import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    # Assert that the __eq__ method works as expected
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    # Assert that the __eq__ method works as expected when url is None
    def test_eq_url_none(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        self.assertIsNone(node.url)
        self.assertIsNone(node2.url)

    # Assert that the __eq__ method works as expected when text_type is different
    def test_eq_text_type_different(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
