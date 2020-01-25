class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class link:
    def __init__(self):
        self.head = node()

# Head node doesnt contain any data just a ponter to fist node
    def append(self,data):
        new_node = node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
#returns length of the list starting from 1 as head doesnt cntain data so start from 1st node
    def length(self):
        start = self.head
        total = 0
        while start.next!= None:
            start = start.next
            total +=1
        return total
#display data of the linked list
    def display(self):
        start = self.head
        while start.next !=None:
            start = start.next
            print(start.data)

# add node inbetween nodes  doesnt add node at last position of the list use append for that
    def insert(self,data,no):
        new_node = node(data)
        prev_node = self.head
        for x in range(no-1):
            prev_node = prev_node.next

        new_node.next = prev_node.next
        prev_node.next = new_node

#deleting node by nunber
    def delete(self,no):
        prev_node = self.head
        second_node = prev_node.next
        for x in range(no-1):
            prev_node = prev_node.next
            second_node = prev_node.next

        prev_node.next = second_node.next





li = link()
li.append(1)
li.append(2)
li.append(3)
print('lenght',li.length())
li.display()

li.insert(8,2)
print('after insertion')
li.display()

li.delete(1)
print('after deletion')
li.display()



