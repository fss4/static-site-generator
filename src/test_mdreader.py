import unittest

from textnode import *
from mdreader import *

class TestMDreaderFuncs(unittest.TestCase):
    def test_converter1(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual([
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ],new_nodes)
        
    def test_converter2(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual([
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ],new_nodes)

    def test_converter3(self):
        node = TextNode("This is text with an _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual([
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ],new_nodes)
        
    def test_converter4(self):
        node = TextNode("_This_ is text with an _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual([
            TextNode("This", TextType.ITALIC),
            TextNode(" is text with an ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ],new_nodes)
        
    def test_converter4(self):
        node = TextNode("_This_ _is_ text with an _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual([
            TextNode("This", TextType.ITALIC),
            TextNode(" ", TextType.TEXT),
            TextNode("is", TextType.ITALIC),
            TextNode(" text with an ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ],new_nodes)

    def test_converter4(self):
        node = TextNode("_This_ _is_ text with an _italic block_ _word_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual([
            TextNode("This", TextType.ITALIC),
            TextNode(" ", TextType.TEXT),
            TextNode("is", TextType.ITALIC),
            TextNode(" text with an ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" ", TextType.TEXT),
            TextNode("word", TextType.ITALIC),
        ],new_nodes)
            
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [link](https://www.google.com)"
        )
        self.assertListEqual([("link", "https://www.google.com")], matches)
        
    def test_extract_markdown_images_with_links(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://www.google.com)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_markdown_links_with_image(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://www.google.com)"
        )
        self.assertListEqual([("link", "https://www.google.com")], matches)
        
    def test_extract_multiple_images(self):
        matches = extract_markdown_images(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and two images\
            ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg), ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        )
        self.assertListEqual([("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"), ("rick roll", "https://i.imgur.com/aKaOqIh.gif")], matches)
        
    def test_extract_multiple_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and two images\
            ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg), ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)


if __name__ == "__main__":
    unittest.main()