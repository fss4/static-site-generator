import unittest

from htmlnode import *
from textnode import *


class TestHTMLNode(unittest.TestCase):
    
    #HTMLNode tests
    def test_basic(self):
        node = HTMLNode("p","How did I get here!")
        self.assertEqual(node.tag,"p")
        self.assertEqual(node.value, "How did I get here!")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
    
    def test_children(self):
        nodec = HTMLNode("p","this is not my beautiful house")
        nodep = HTMLNode("h1","with a beautiful house",nodec,{"href":"https://www.youtube.com/watch?v=5IsSpAOD6K8"})
        self.assertEqual(nodep.children.value,"this is not my beautiful house")
        self.assertEqual(list(nodep.props.keys()),["href"])
    
    def test_props_to_html(self):
        node = HTMLNode("h1","with a beautiful house",None,{"href": "https://www.google.com", "target": "_blank",})
        res = node.props_to_html()
        self.assertEqual(res,' href="https://www.google.com" target="_blank"')
    
    #LeafNode tests
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(value="Once in a Lifetime",props={"href":"https://www.youtube.com/watch?v=5IsSpAOD6K8"})
        self.assertEqual(node.to_html(),"Once in a Lifetime")
        
    def test_leaf_to_html_tag(self):
        node = LeafNode('a',"Once in a Lifetime",{"href":"https://www.youtube.com/watch?v=5IsSpAOD6K8"})
        self.assertEqual(node.to_html(),'<a href="https://www.youtube.com/watch?v=5IsSpAOD6K8">Once in a Lifetime</a>')
        
    def test_leaf_to_html_img(self):
        node = LeafNode('img',"",{"src": "https://upload.wikimedia.org/wikipedia/en/2/2d/TalkingHeadsRemaininLight.jpg",
                                  "alt" : "Remain in Light album cover",
                                  }
                        )
        self.assertEqual(node.to_html(),'<img src="https://upload.wikimedia.org/wikipedia/en/2/2d/TalkingHeadsRemaininLight.jpg" alt="Remain in Light album cover" />')
        
    def test_leafnode_error(self):
        node = LeafNode(tag="p")
        with self.assertRaises(ValueError):
            node.to_html()
        
    #ParentNode tests
    def test_to_html_no_children(self):
        parent_node = ParentNode("div")
        with self.assertRaises(ValueError):
            parent_node.to_html()
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_multiple_children(self):
        grandchild_node_1 = LeafNode("b", "Once")
        grandchild_node_2 = LeafNode("p", "In a")
        grandchild_node_3 = LeafNode("i", "Lifetime")
        child_node_1 = ParentNode("span", [grandchild_node_1, grandchild_node_2])
        child_node_2 = ParentNode("span", [grandchild_node_3])
        parent_node = ParentNode("div", [child_node_1, child_node_2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>Once</b><p>In a</p></span><span><i>Lifetime</i></span></div>",
        )
    
    
    #text to html tests
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
        
    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")
        
    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")
    
    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        html_result = html_node.to_html()
        self.assertEqual(html_result, '<a href="www.google.com">This is a link node</a>')
    
    def test_image(self):
        node = TextNode("boot dot dev logo", TextType.IMAGE, "https://www.boot.dev/img/bootdev-logo-full-150.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        html_result = html_node.to_html()
        self.assertEqual(html_result, '<img src="https://www.boot.dev/img/bootdev-logo-full-150.png" alt="boot dot dev logo" />')
        
if __name__ == "__main__":
    unittest.main()