from textnode import *

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        res = ""
        for key in self.props.keys():
            res += f' {key}="{self.props[key]}"'
        return res
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        elif self.props is None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        elif self.tag == 'img':
            props = self.props_to_html()
            return f'<{self.tag}{props} />'
        else:
            props = self.props_to_html()
            return f'<{self.tag}{props}>{self.value}</{self.tag}>'
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError
        if self.children is None:
            raise ValueError
        else:
            res = f'<{self.tag}>'
            for child in self.children:
                res += child.to_html()
            res += f'</{self.tag}>'
        return res
    
def text_node_to_html_node(text_node):
    match text_node.text_type.name:
        case "TEXT":
            return LeafNode(value=text_node.text)
        case "BOLD":
            return LeafNode('b', text_node.text)
        case "ITALIC":
            return LeafNode('i', text_node.text)
        case "CODE":
            return LeafNode('code', text_node.text)
        case "LINK":
            return LeafNode('a', text_node.text, {"href" : text_node.url})
        case "IMAGE":
            return LeafNode('img', "", {"src" : text_node.url,
                                        "alt" : text_node.text,
                                        }
                            )
        case _:
            raise Exception("The TextNode given is not one of the required types")