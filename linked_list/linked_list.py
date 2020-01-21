class node:
    def __init__(self, data= None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self,data):
        new_node = node(data)
        crnt =self.head
        while crnt.next != None:
            crnt = crnt.next
        crnt.next = new_node

    def length(self):
        length = 0
        start  = self.head
        while start.next != None:
            length += 1
            start = start.next
        return length

    def display(self):
        data = []
        start = self.head
        while start.next != None:
            start = start.next
            data.append(start.data)
        return(data)


l = linked_list()
print(l.length())
l.append(3)
l.append(2)
l.append(4)
print(l.length())
print(l.display())

