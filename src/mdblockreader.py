import textwrap
from enum import Enum

class BlockType(Enum):
    PARA = "paragraph"
    HEAD = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered list"
    OLIST = "ordered list"
    
def markdown_to_blocks(markdown):
    text = textwrap.dedent(markdown)
    blocks = text.split('\n\n')
    new_blocks = []
    
    for block in blocks:
        block = block.replace("    ", "\t")
        new_blocks.append("".join(block.strip()))
    new_blocks = list(filter(None,new_blocks))
    return new_blocks

def block_to_block_type(block):
    if '#' == block[0]:
        i = 0
        while block[i] == "#":
            i += 1
        if block[i] == ' ' and i <= 6:
            return BlockType.HEAD
        return BlockType.PARA
    
    elif '```\n' == block[0:4] and block[-4:] == '\n```':
        return BlockType.CODE
    
    elif block[0] == '>':
        check = block.split('\n')
        for line in check[1:]:
            if line[0] == '>':
                continue
            else:
                return BlockType.PARA
        return BlockType.QUOTE
    
    elif block[0:2] == '- ':
        check = block.split("\n")
        for line in check[1:]:
            if line[0:2] == '- ':
                continue
            else:
                return BlockType.PARA
        return BlockType.ULIST
    
    elif block[0:3] == "1. ":
        check = block.split("\n")
        num = 1
        for line in check[1:]:
            num += 1
            if line[0:3] == f'{num}. ':
                continue
            else:
                return BlockType.PARA
        return BlockType.OLIST
    
    else:
        return BlockType.PARA
    
