class Node:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data > node.data:
            if node.right:
                self.insert_node(data,node.right)
            node.right = Node(data)



    def display (self):
        b = self.root.right
        print(self.root.data,b.data)

t = tree()
t.insert(5)
t.insert(10)
t.display()

