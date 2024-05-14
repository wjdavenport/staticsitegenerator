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

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        if self.children is None:
            raise ValueError("ParentNode requires children")
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode requires a tag")
        print(f"self.children: {self.children}")
        if (self.children is None) or len(self.children) == 0:
            raise ValueError("ParentNode requires children")

        # Convert properties to HTML attributes string, if any
        props_html = self.props_to_html()

        # Initialize the HTML representation of the node with its tag and properties
        html = f"<{self.tag}{props_html}>"

        # Include the node's own value, if any
        if hasattr(self, 'value') and self.value:
            html += str(self.value)

        # Recursively append HTML representation of each child
        for child in self.children:
            html += child.to_html()

        # Close the current tag
        html += f"</{self.tag}>"

        return html


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        if self.children is not None:
            raise ValueError("LeafNode cannot have children")
        
        