class Node:
    def __init__(self,data):
        self.data = data
        self.next  = None

        print(self.data)

class LinkedList:
    def __init__(self):
        self.headval = None

    def insert(self):
        value = input('Node Value:')
        if  self.headval == None:
            self.headval = Node(value)
        else:
            print('walah')


l = LinkedList()
while True:
    usr_inp = input('1->input , anything else quit')
    if usr_inp == '1':
        l.insert()
    else:break


