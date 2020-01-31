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

        print(node.data, end=" ")
        
        if node.right:
            self.trv(node.right)
            
    #travering PREORDER 
    def trv_pre(self,node):
        print(node.data, end=" ")
        if node.left:
            self.trv_pre(node.left)
        
        if node.right:
            self.trv_pre(node.right)

    #travering POSTORDER 
    def trv_post(self, node):
        if node.left:
            self.trv_post(node.left)

        if node.right:
            self.trv_post(node.right)
        print(node.data , end =" ")


    #level order traversal BREADTH FIRST SEARCH
    def level(self,node):
        que = []
        que.insert(0,node)
        
        while que:
            last_n = que[-1]
            if last_n.left:
                que.insert(0,last_n.left)
            
            if last_n.right:
                que.insert(0,last_n.right)
                
            print(last_n.data,end=" ")
            del que[-1]
        



    def display (self):
        print('\nwallah inorder traverse:', end =" ")
        if self.root:
            self.trv(self.root)
 
        print('\nwallah preorder traverse:', end=" ")
        if self.root:
            self.trv_pre(self.root)

        print('\nwallah postorder treversal:',end=" ")
        if self.root:
            self.trv_post(self.root)

        print('\nwallah  level order traversal:', end=" ")
        if self.root:
            self.level(self.root)
        

t = tree()
t.insert(50)
t.insert(20)
t.insert(10)
t.insert(30)
t.insert(60)
t.insert(55)
t.insert(70)
t.display()

