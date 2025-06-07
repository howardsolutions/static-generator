import json

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError("to_html not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        
        props_list = []
        
        for key, value in self.props.items():
            if isinstance(value, str):
                props_list.append(f'{key}="{value}"')
            else:
                props_list.append(f'{key}={value}')
        return " ".join(props_list)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {json.dumps(self.props)})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("value is required")
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("value is required")
 
        if self.tag is not None:
            props_html = self.props_to_html()
            if props_html:
                return f"<{self.tag} {props_html}>{self.value}</{self.tag}>"
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return self.value


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None or children is None:
            raise ValueError("tag and children are required")
        if not all(isinstance(child, HTMLNode) for child in children):
            raise ValueError("all children must be HTMLNode instances")
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("tag is required")
        
        if self.children is None:
            raise ValueError("children is required")
            
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
            
        props_html = self.props_to_html()
        if props_html:
            return f"<{self.tag} {props_html}>{children_html}</{self.tag}>"
        
        return f"<{self.tag}>{children_html}</{self.tag}>"
