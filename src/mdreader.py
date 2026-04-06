import re

from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type.value != "text":
            new_nodes.append(node)
        if delimiter not in node.text:
            raise Exception("delimiter {delimiter} not found. Invalid markdown syntax.")
        new_nodes_text = (node.text).split(f"{delimiter}")
        check = 0
        for new in new_nodes_text:
            if check % 2 == 1:
                new_nodes.append(TextNode(new, text_type))
            else:
                if new:
                    new_nodes.append(TextNode(new,TextType.TEXT))
            check += 1            
    return new_nodes

def extract_markdown_images(text):
    #This checks for md links which are of the form ![alt text](url or path)
    regex = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(regex, text)
    return matches

def extract_markdown_links(text):
    #This checks for md links which are of the form [link](url) but DO NOT have a ! prefixing them
    regex = r"(?<!!)\[(.*?)\]\((.*?)\)"
    matches = re.findall(regex, text)
    return matches