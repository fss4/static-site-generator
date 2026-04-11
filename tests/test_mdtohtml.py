import unittest

from textnode import *
from mdinlinereader import *
from mdblockreader import *
from htmlnode import *
from mdtohtml import *

class TestMDToHTML(unittest.TestCase):

    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    def test_actual_codeblock(self):
        md = """
            ```
            def func():
                pass
            ```
            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>def func():\n\tpass\n</code></pre></div>",
        )
    
    def test_general_md_block_good(self):
        self.maxDiff = None
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
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>This is a heading</h3><p>####### This should be a paragraph</p><pre><code>def func():\n\tpass\n</code></pre><blockquote>“I have not failed. I've just found 10,000 ways that won't work.”\n" \
            "-Thomas Edison</blockquote><ul><li>This is a list</li><li>with items</li></ul><ol><li>This is an ordered list.</li><li>With items</li></ol></div>",
        )
        
    def test_general_md_block_bad(self):
        self.maxDiff = None
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
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>This is a maximal heading</h6><p>####### This should be a paragraph</p><pre><code>def func():\n\tpass\n</code></pre><blockquote>“I have not failed. I've just found 10,000 ways that won't work.”\n" \
            "-Thomas Edison</blockquote><p>-This is a list - with items</p><p>1. This is an ordered list. 2.With items</p></div>",
        )
if __name__ == "__main__":
    unittest.main()