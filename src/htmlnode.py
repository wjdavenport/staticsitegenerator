class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode requires a value")
        if self.tag is None:
            return str(self.value)
        else:
            props_html = self.props_to_html()
            return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for key, value in self.props.items():
            props_html += f" {key}=\"{value}\""
        return props_html
    
    def __repr__(self):
        return f"HTMLNode(tag='{self.tag}', value='{self.value}', children={self.children}, props={self.props})"

    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        if self.children is not None:
            raise ValueError("LeafNode cannot have children")
        
        