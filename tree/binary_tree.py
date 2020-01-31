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
            else:
                node.right = Node(data)

        else:
            if node.left:
                self.insert_node(data, node.left)
            else:
                node.left = Node(data)


#traversing tree INORDER
    def traverse(self,node):
        if node.left:
            self.traverse(node.left)

        print(node.data)
        
        if node.right:
            self.traverse(node.right)
            
#travering PREORDER
    def traverse_pre(self,node):
        print(node.data)
        if node.left:
            self.traverse_pre(node.left)
        
        if node.right:
            self.traverse_pre(node.right)


    def display (self):
        print('wallah inorder traverse.')
        if self.root:
            self.traverse(self.root)

        print('wallah preorder traverse.')
        if self.root:
            self.traverse_pre(self.root)

    
        

t = tree()
t.insert(50)
t.insert(20)
t.insert(10)
t.insert(30)
t.insert(60)
t.insert(55)
t.insert(70)
t.display()

