import re

from textnode import *


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

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type.value != "text":
            new_nodes.append(node)
            continue
        new_nodes_text = (node.text).split(f"{delimiter}")
        if len(new_nodes_text) % 2 == 0:
            raise Exception("odd number of delimiters {delimiter} found. Invalid markdown syntax. All delimiters must close.")
        check = 0
        for new in new_nodes_text:
            if check % 2 == 1:
                new_nodes.append(TextNode(new, text_type))
            else:
                if new:
                    new_nodes.append(TextNode(new,TextType.TEXT))
            check += 1            
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        #if a node is already not a text node we add it and move on, assuming its already formatted..
        if node.text_type.value != "text":
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        #If there are no images in the node we move on to the next one
        if not images:
            new_nodes.append(node)
            continue
        #we will only look at the first image and then recur on the set of created nodes. The already formatted images will be ignored due to the first if statement.
        img = images[0]
        imgtxt =  f'![{img[0]}]({img[1]})'
        #we must escape the string we want to split on as it contains characters that mean something in regex.
        new_nodes_text = re.split(f'({re.escape(imgtxt)})', node.text)
        check = 0
        #cycle through the split text.  The copies of the image will appear on odd-indexed elements.
        for new in new_nodes_text:
            if check % 2 == 1:
                new_nodes.append(TextNode(img[0], TextType.IMAGE, img[1]))
            else:
                if new:
                    new_nodes.append(TextNode(new,TextType.TEXT))
            check += 1
        #once the new nodes are set up recur to format the remaining images
        new_nodes = split_nodes_image(new_nodes) 
    return new_nodes

#this function is almost identical to the previous one. All comments more or less carry over.
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        #if a node is already not a text node we add it and move on, assuming its already formatted. This could cause issues with bold links etc.
        if node.text_type.value != "text":
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue
        lnk = links[0]
        lnktxt =  f'[{lnk[0]}]({lnk[1]})'
        new_nodes_text = re.split(rf'(?<!!)({re.escape(lnktxt)})', node.text)
        check = 0
        for new in new_nodes_text:
            if check % 2 == 1:
                new_nodes.append(TextNode(lnk[0], TextType.LINK, lnk[1]))
            else:
                if new:
                    new_nodes.append(TextNode(new,TextType.TEXT))
            check += 1
        new_nodes = split_nodes_link(new_nodes) 
    return new_nodes

def text_to_textnodes(text):
    nodes = split_nodes_delimiter([TextNode(text,TextType.TEXT)], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
