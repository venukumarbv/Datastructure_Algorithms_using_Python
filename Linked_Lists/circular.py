class Node:
    '''A Class to create a Node object'''
    def __init__(self,value):
        self.info = value
        self.link = None

class CircularLinkedList:
    '''A Class to create and Modify Circular Linked List'''
    def __init__(self):
        self.last = None

    def insert_in_empty(self, value):
        temp = Node(value)
        self.last = temp
        self.last.link = self.last

    def insert_in_beginning(self, value):
        if self.last is None: # If Empty
            self.insert_in_empty(value)
            return

        temp = Node(value)
        temp.link = self.last.link
        self.last.link = temp

    def insert_at_end(self,value):
        if self.last is None:
            self.insert_in_empty(value)
            return

        temp = Node(value)
        temp.link = self.last.link
        self.last.link = temp
        self.last = temp

    def createList(self):
        n = int(input("Enter Number of Nodes "))
        if n == 0:
            print("Number of nodes should be greater than 0 ")
            self.createList()

        for i in range(n):
            value = int(input("Enter the value of {} node".format(i+1)))
            self.insert_at_end(value)

    def insert_after_node(self,x, value):
        p = self.last.link # Point P to the first node

        while True:
            if p.info == x:
                break
            p = p.link
            if p == self.last.link:
                break

        if p == self.last.link and p.info != x:
            print(x, " Not found in the Circular List")
            return
        else:
            temp = Node(value)
            temp.link = p.link
            p.link = temp
            if p == self.last:
                self.last = temp

    def display(self):
        if self.last is None:
            print("The list is Empty")
            return
        p = self.last.link # Point to the First node
        while True:
            print("-->",p.info,end='')
            p = p.link
            if p == self.last.link: # If it comes back to the same position as started
                break
        print()

    def delete_first_node(self):
        # If node is Empty
        if self.last is None:
            print("The Node is Empty")
            return
        # If only node
        if self.last.link == self.last:
            self.last = None
        # Otherwise
        self.last.link = self.last.link.link

    def delete_last_node(self):
        # If node is Empty
        if self.last is None:
            print("The Node is Empty")
            return
        if self.last.link == self.last:
            self.last = None
        # Otherwise fid the predecessor P
        p = self.last.link
        while p.link != self.last:
            p = p.link
        p.link = self.last.link
        self.last = p

    def delete_a_node(self, x):
        if self.last is None:
            print("The List is Empty")
            return
        if self.last.link == self.last and self.last.info == x:
            self.last = None
            return
        if self.last.link.info == x:
            self.last.link = self.last.link.link
            return

        p = self.last.link
        while p.link != self.last.link: # Stop at last node
            if p.info == x:
                break
            p = p.link
        if p == self.last.link:
            print(x, "is not found in the list")
            return
        else:
            p.link = p.link.link
            if self.last.info == x:
                self.last = p

clist = CircularLinkedList()
clist.createList()

while True:
    print(('*' * 20) + '**  Menu  **' + ('*' * 20))
    print('\t\t1.Display the List')
    print('\t\t2.Insert at the Beginnig')
    print('\t\t3.Insert at the End')
    print('\t\t4.Insert after a node')
    print('\t\t5.Delete First Node')
    print('\t\t6.Delete the Last Node')
    print('\t\t7.Delete a node')
    print('\t\t20.Quit')
    op = int(input('Enter your option: '))

    if op == 1:
        clist.display()
    elif op == 2:
        data = int(input('Enter a value to insert: '))
        clist.insert_in_beginning(data)
    elif op == 3:
        data = int(input('Enter a value to insert: '))
        clist.insert_at_end(data)
    elif op == 4:
        clist.display()
        x = int(input("Enter the node after which a new node to be inserted: "))
        value = int(input("Enter the value of the new node: "))
        clist.insert_after_node(x, value)
    elif op == 5:
        clist.delete_first_node()
    elif op == 6:
        clist.delete_last_node()
    elif op == 7:
        clist.display()
        x = int(input("Enter the node to be deleted "))
        clist.delete_a_node(x)
    elif op == 20:
        exit(0)