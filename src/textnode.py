from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    
class TextNode():
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self,other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        else:
            return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

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
 #NEED TO DEAL WIITH THE CASE WHEN THE NODE IS AT THE FRONT OF THE SENTENCE. THERE IS A EMPTY STRING THAT NEEDS TO BE DEALT WITH CORRECTLY.
            if check % 2 == 1:
                new_nodes.append(TextNode(new, text_type))
            else:
                if new:
                    new_nodes.append(TextNode(new,TextType.TEXT))
            check += 1            
    return new_nodes
