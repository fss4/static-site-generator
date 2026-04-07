from textnode import *
from htmlnode import *
from mdreader import *

def main():
    '''
    dummy = TextNode("hello world",TextType.TEXT)
    test = text_node_to_html_node(dummy)
    print(dummy)
    print(test.to_html())
    node = TextNode("This is a link node", TextType.LINK, "www.google.com")
    html_node = text_node_to_html_node(node)
    print(html_node.to_html() )
    leaf = LeafNode('p','Hello World!')
    print(leaf.to_html())
    text = "This is text with a link [to boot dev](https://www.boot.dev) and two images ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
    print(extract_markdown_images(text))
    print(extract_markdown_links(text))
    node = TextNode(text,TextType.TEXT,)
    print('-'*100)
    print(node)
    print("-"*100)
    print(split_nodes_link([node]))
    '''
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    print(text_to_textnodes(text))
main()