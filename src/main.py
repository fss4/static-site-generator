from textnode import *
from htmlnode import *
from mdreader import *

def main():
    dummy = TextNode("hello world",TextType.TEXT)
    test = text_node_to_html_node(dummy)
    print(dummy)
    print(test.to_html())
    node = TextNode("This is a link node", TextType.LINK, "www.google.com")
    html_node = text_node_to_html_node(node)
    print(html_node.to_html() )
    leaf = LeafNode('p','Hello World!')
    print(leaf.to_html())
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and two images\
        ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg), ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
    print(extract_markdown_images(text))
    print(extract_markdown_links(text))
main()