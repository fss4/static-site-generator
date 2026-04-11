from htmlnode import *
from mdblockreader import *
from mdinlinereader import *


    
def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match block_type.name:
        case "PARA":
            node = ParentNode(
                tag = "p",
                )
        case "HEAD":
            count = 0
            while block[count] == "#":
                count += 1
            t = f'h{count}'
            node = ParentNode(
                tag = t,
                )
        case "CODE":
            node = ParentNode(
                tag = "pre",
                )
        case "QUOTE":
            node = ParentNode(
                tag = "blockquote",
                )
        case "ULIST":
            node = ParentNode(
                tag = "ul",
                )
        case "OLIST":
            node = ParentNode(
                tag = "ol",
                )
        case _:
            raise Exception(f"Block {block[0:20]}... is not one of the allowed types")
    return node
            
def text_to_children(block):
    block_type = block_to_block_type(block)
    res = []
    if block_type.name[1:] == "LIST":
        lines = block.split("\n")
        for line in lines:
            line = line.split(" ",1)[1]
            textnodes_line = text_to_textnodes(line)
            html_lines = []
            for tn_line in textnodes_line:
                html_lines.append(text_node_to_html_node(tn_line))
            res.append(ParentNode(tag="li",children=html_lines))
        return res
    
    elif block_type.name == "PARA":
        new_pblock = block.replace("\n", " ")
        tnodes = text_to_textnodes(new_pblock)
        for node in tnodes:
            res.append(text_node_to_html_node(node))
        return res
    
    elif block_type.name == "HEAD":
        count = 0
        while block[count] == "#":
            count += 1
        block = block[count+1:]
        tnodes = text_to_textnodes(block)
        for node in tnodes:
            res.append(text_node_to_html_node(node))
        return res
    
    elif block_type.name == "QUOTE":
        lines = block.split('\n')
        new_lines = []
        for line in lines:
            if line[1] == " ":
                new_lines.append(line[2:])
            else:
                new_lines.append(line[1:])
        block = "\n".join(new_lines)
        tnodes = text_to_textnodes(block)
        for node in tnodes:
            res.append(text_node_to_html_node(node))
        return res
    
    else:
        tnodes = text_to_textnodes(block)
        for node in tnodes:
            res.append(text_node_to_html_node(node))
        return res
    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    ls = []
    for block in blocks:
        blocknode = block_to_html_node(block)
        if blocknode.tag != "pre":
            blocknode.children = text_to_children(block)
        else:
            block = block[4:-3]
            codenode = TextNode(block,TextType.CODE)
            blocknode.children = [text_node_to_html_node(codenode)]
            
        ls.append(blocknode)
    parent = ParentNode(tag = "div", children = ls)
    return parent
                

        