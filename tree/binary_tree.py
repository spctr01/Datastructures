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
        else:
            self.insert_node(data, self.root)
        

    def insert_node(self, data, node):
        if data > node.data:
            if node.right:
                self.insert_node(data,node.right)
            node.right = Node(data)

        else:
            if node.left:
                self.insert_node(data, node.left)
            node.left = Node(data)


#traversing tree INORDER
    def traverse(self,node):
        if node.left:
            self.traverse(node.left)

        print(node.data)
        
        if node.right:
            self.traverse(node.right)
        


    def display (self):
        if self.root:
            self.traverse(self.root)
        

t = tree()
t.insert(5)
t.insert(10)
t.display()

