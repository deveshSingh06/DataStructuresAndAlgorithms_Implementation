#Tree Implementation

class node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class tree:
    def createNode(self, value):
        node(value)

    def insert(self, node, value):
        if node is None:
            self.createNode(value)
        if value<node.data:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)
        return node
