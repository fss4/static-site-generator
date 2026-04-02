from textnode import *
from htmlnode import *

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
    
main()