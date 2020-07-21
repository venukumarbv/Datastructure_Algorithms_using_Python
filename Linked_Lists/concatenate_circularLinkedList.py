class Node:
    def __init__(self,value):
        self.info = value
        self.link = None

class CircularLinkedList:
    def __init__(self):
        self.last = None

    def insert_a_node(self, value):
        temp = Node(value)

        if self.last is None: # Create a logical cicular list during empty list
            self.last = temp
            self.last.link = self.last

        # insert at end
        temp.link = self.last.link
        self.last.link = temp
        self.last = temp

    def create_list(self):
        n = int(input("Enter number of Nodes: "))
        for i in range(n):
            value = int(input("Enter the vale of {} node ".format(i+1)))
            self.insert_a_node(value)

    def display(self):
        if self.last is None:
            print("The List is Empty")
            return
        p = self.last.link
        while True:
            print('-->', p.info, end='')
            p = p.link
            if p == self.last.link:
                break
        print()

    def concatenate(self, list2):
        if self.last is None:
            self.last = list2.last.link
            return

        if list2.last is None:
            return

        p = self.last.link
        self.last.link = list2.last.link
        list2.last.link = p
        self.last = list2.last

clist1 = CircularLinkedList()
clist2 = CircularLinkedList()

print("List 1")
clist1.create_list()
print("List 2")
clist2.create_list()

print("The List 1 is:")
clist1.display()
print("The List 2 is:")
clist2.display()

print("Concatenated List is :")
clist1.concatenate(clist2)
clist1.display()