class Node:
    '''A class to create a Node'''

    def __init__(self, value):
        self.info = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    '''A Class to perform action on Doubly linked List'''

    def __init__(self):
        self.start = None

    def createList(self):
        n = int(input("Enter Number of Nodes to be Inserted: "))
        for i in range(n):
            value = int(input("Enter the value of {} node ".format(i + 1)))
            self.insert_at_end(value)

    def display(self):
        if self.start is None:
            print("The List is Empty")
            return

        p = self.start
        print("The List is" + "\n")
        print("start", end='')
        while p is not None:
            print(' <==> ',p.info, end='')
            p = p.next
        print(" <==> None")

    def insert_at_beginning(self, value):
        temp = Node(value)
        if self.start is None:  # If empty List
            self.start = temp
            return

        p = self.start
        temp.next = self.start
        self.start.prev = temp
        self.start = temp

    def insert_at_end(self, value):
        temp = Node(value)
        if self.start is None:  # If empty List
            self.start = temp
            return
        p = self.start
        while p.next is not None:
            p = p.next
        p.next = temp
        temp.prev = p

    def insert_after_node(self, value, x):
        temp = Node(value)
        p = self.start
        while p is not None:
            if p.info == x:
                temp.prev = p
                if p.next is not None:  # Should not do if the x is last node
                    temp.next = p.next
                    p.next.prev = temp  # Should not do if the x is last node
                p.next = temp
                break
            p = p.next
        else:  # if the node is not found ; no break in the while loop
            print("The node {} is not present in the list".format(x))

    def insert_before_node(self, value, x):
        if self.start is None:
            print("The list is Empty ")
            return

        if self.start.info == x: # Node found at first place
            self.insert_at_beginning(value) # Insert at the beginning
            return

        temp = Node(value)
        p = self.start
        while p is not None:
            if p.info == x: # node found
                temp.prev = p.prev
                temp.next = p
                p.prev.next = temp
                p.prev = temp
                break
            p = p.next
        else:
            print('The node {} is not found in the list'.format(x))

    def delete_first_node(self):
        # If the node is Empty
        if self.start is None:
            print("The List is Empty")
            return
        # Check if only one node is present
        if self.start.next is None:
            self.start = None # Delete the firs node by assigning start to None
            return
        # If there are multiple nodes
        self.start = self.start.next
        self.start.prev = None

    def delete_last_node(self):
        # Check for the empty list
        if self.start is None:
            print("The list is Empty")
            return
        # Check if only one node is present
        if self.start.next is None:
            self.start = None
            return

        # Otherwise
        p = self.start
        while p.next is not None: # Goto last node of the list
            p = p.next
        p.prev.next = None

    def delete_a_node(self, x):
        # Check if node is Empty
        if self.start is None:
            print("The list is Empty")
            return

        if self.start.next is None: # if only one node is present
            if self.start.info == x:
                self.start = None
            else:
                print(x,"is not found in the list")
            return

        if self.start.info == x: # if found at the first place itself
            self.start = self.start.next
            self.start.prev = None
            return

        p = self.start
        while p.next is not None:
            if p.info == x:
                p.prev.next = p.next
                p.next.prev = p.prev
                break
            p = p.next

        else: # p is pointing to last node now
            if p.info == x: # if last node is the node to be deleted
                p.prev.next = None
            else: # if not , p has traversed all the nodes and node to be deleted not found
                print(x,"is not found in the list")

    def reverse_list(self):
        if self.start is None:
            print("The list is empty ")
            return

        p1 = self.start
        p2 = p1.next
        p1.next = None
        p1.prev = p2

        while p2 is not None:
            p2.prev = p2.next
            p2.next = p1
            p1 = p2
            p2 = p2.prev

        self.start = p1

dlist = DoubleLinkedList()
dlist.createList()
print()

while True:
    print(('*' * 20) + '**  Menu  **' + ('*' * 20))
    print('\t\t1.Display the List')
    print('\t\t2.Insert at the Beginnig')
    print('\t\t3.Insert at the End')
    print('\t\t4.Insert after a node')
    print('\t\t5.Insert before a node')
    print('\t\t6.Delete the First node')
    print('\t\t7.Delete the Last node')
    print('\t\t8.Delete a node')
    print('\t\t9.Reverse the List')
    print('\t\t20.Quit')
    op = int(input('Enter your option: '))

    if op == 1:
      dlist.display()
    elif op == 2:
        data = int(input('Enter a value to insert: '))
        dlist.insert_at_beginning(data)
    elif op == 3:
        data = int(input('Enter a value to insert: '))
        dlist.insert_at_end(data)
    elif op == 4:
        dlist.display()
        x = int(input("Enter the node after which a new node to be inserted: "))
        value = int(input("Enter the value of the new node: "))
        dlist.insert_after_node(value, x)
    elif op == 5:
        dlist.display()
        x = int(input("Enter the node before which a new node to be inserted: "))
        value = int(input("Enter the value of the new node: "))
        dlist.insert_before_node(value, x)

    elif op == 6:
        dlist.delete_first_node()

    elif op == 7:
        dlist.delete_last_node()

    elif op == 8:
        dlist.display()
        node = int(input("Enter the Node to be deleted"))
        dlist.delete_a_node(node)

    elif op == 9:
        dlist.reverse_list()

    elif op == 20:
        exit(0)
