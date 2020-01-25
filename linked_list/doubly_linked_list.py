class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
        self.prev = None


class doubly:
    def __init__(self):
        self.head = node()

    def append(self,data):
        new_node = node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def display(self):
        start = self.head
        while start.next != None:
            start = start.next
            print(start.data)

    def length(self):
        l = 0
        start = self.head
        while start.next != None:
            start = start.next
            l += 1
        return l

# add node inbetween nodes  doesnt add node at last position of the list use append for that
    def insert(self, data, position):
        new_node = node(data)
        start = self.head
        next_node = start.next
        for x in range(position-1):
            start = start.next
            next_node = start.next
        start.next = new_node
        next_node.prev = new_node
        new_node.prev = start
        new_node.next = next_node

#delete node by its postion in linked list
    def delete(self, position):
        start = self.head
        next_node = start.next
        for x in range(position-1):
            start = start.next
            next_node = start.next
        if next_node.next == None:
            start.next = None
            next_node.prev = None
        else:
            next_node = next_node.next
            next_node.prev = start
            start.next = next_node

        


d = doubly()
d.append(1)
d.append(2)
d.display()

d.insert(3,1)
print('after insertion')
d.display()

print('lenght', d.length() )

d.delete(3)
print('after deletion')
d.display()

