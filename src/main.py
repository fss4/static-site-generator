from textnode import *
from htmlnode import *
from mdinlinereader import *
from mdblockreader import *
import sys
import os

def main():
    md = """
            ### This is a heading

            ####### This should be a paragraph
            
            ```
            def func():
                pass
            ```
            
            > “I have not failed. I've just found 10,000 ways that won't work.”
            > -Thomas Edison

            - This is a list
            - with items
            
            1. This is an ordered list.
            2. With items
            """
    blocks = markdown_to_blocks(md)
    for block in blocks:
        block_to_block_type(block)
    
    print(sys.path)
    print("PYTHONPATH =", os.environ.get("PYTHONPATH"))
main()