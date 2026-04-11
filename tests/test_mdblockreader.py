import unittest

from textnode import *
from mdinlinereader import *
from mdblockreader import *

class TestMDblockReaderFuncs(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        
    def test_markdown_to_blocks_more_newlines(self):
        md = """
            This is **bolded** paragraph
            
            
            
            

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        
    def test_markdown_to_blocks_weird_tabs(self):
        md = """
            This is **bolded** paragraph
            
            
            
            

                    This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_1(self):
        md = """
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """
        blocks = markdown_to_blocks(md)
        block_type = []
        for block in blocks:
            block_type.append(block_to_block_type(block))
        self.assertEqual(
            block_type,
            [
                BlockType.PARA,
                BlockType.PARA,
                BlockType.ULIST,
            ]
        )
        
    def test_markdown_to_blocks_2(self):
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
        block_type = []
        for block in blocks:
            block_type.append(block_to_block_type(block))
        self.assertEqual(
            block_type,
            [
                BlockType.HEAD,
                BlockType.PARA,
                BlockType.CODE,
                BlockType.QUOTE,
                BlockType.ULIST,
                BlockType.OLIST,
            ]
        )
        
    def test_markdown_to_blocks_3(self):
        md = """
             This is a heading

            ####### This should be a paragraph
            
            ```
            def func():
                pass
            
            > “I have not failed. I've just found 10,000 ways that won't work.”
             -Thomas Edison

            - This is a list
            -with items
            
            1. This is an ordered list.
            With items
            """
        blocks = markdown_to_blocks(md)
        block_type = []
        for block in blocks:
            block_type.append(block_to_block_type(block))
        self.assertEqual(
            block_type,
            [
                BlockType.PARA,
                BlockType.PARA,
                BlockType.PARA,
                BlockType.PARA,
                BlockType.PARA,
                BlockType.PARA,
            ]
        )
    def test_markdown_to_blocks_4(self):
        md = """
            ###### This is a maximal heading

            ####### This should be a paragraph
            
            ```
            def func():
                pass
            ```
            
            > “I have not failed. I've just found 10,000 ways that won't work.”
            >-Thomas Edison

            -This is a list
            - with items
            
            1. This is an ordered list.
            2.With items
            """
        blocks = markdown_to_blocks(md)
        block_type = []
        for block in blocks:
            block_type.append(block_to_block_type(block))
        self.assertEqual(
            block_type,
            [
                BlockType.HEAD,
                BlockType.PARA,
                BlockType.CODE,
                BlockType.QUOTE,
                BlockType.PARA,
                BlockType.PARA,
            ]
        )
if __name__ == "__main__":
    unittest.main()