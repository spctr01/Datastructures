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
    def trv(self,node):
        if node.left:
            self.trv(node.left)

        print(node.data)
        
        if node.right:
            self.trv(node.right)
            
#travering PREORDER
    def trv_pre(self,node):
        print(node.data)
        if node.left:
            self.trv_pre(node.left)
        
        if node.right:
            self.trv_pre(node.right)


    def trv_post(self, node):
        if node.left:
            self.trv_post(node.left)
        

        if node.right:
            self.trv_post(node.right)
        print(node.data)

    def display (self):
        print('wallah inorder traverse.')
        if self.root:
            self.trv(self.root)
 
        print('wallah preorder traverse.')
        if self.root:
            self.trv_pre(self.root)

        print('wallah postorder treversal')
        if self.root:
            self.trv_post(self.root)

    
        

t = tree()
t.insert(50)
t.insert(20)
t.insert(10)
t.insert(30)
t.insert(60)
t.insert(55)
t.insert(70)
t.display()

