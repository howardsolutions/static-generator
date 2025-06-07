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
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"