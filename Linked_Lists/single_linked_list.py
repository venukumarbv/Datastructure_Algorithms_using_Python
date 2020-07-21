class Node:
    ''' A class to create a node with the given value'''

    def __init__(self, value):
        self.value = value  # Value of the item
        self.link = None  # Link of the node, initially set to None


class SingleLinkedList:
    ''' Class for all the operations on Single Linked List'''

    # ******************************* Creating a list ******************
    def __init__(self):
        self.start = None  # A reference to the beginning of the Node

    def create_list(self):
        n = int(input("Enter Number of nodes: "))
        if n == 0:
            print("Number of nodes must be more than 0")
            self.create_list()

        for i in range(n):
            value = int(input('Enter the value of node {}: '.format(i+1)))
            self.insert_at_end(value)

    def search_in_list(self, x):
        if self.start is None:
            print("The List is Empty")
            return
        else:
            pos = 1
            p = self.start
            while p is not None:
                if p.value == x:
                    print(x, "is found at:", pos)
                    break
                pos += 1
                p = p.link
            else:
                print(x, "is not present in the list")
                return

    # ******************* Insertion *******************************

    def insert_at_beginning(self, value):
        temp = Node(value)
        temp.link = self.start
        self.start = temp

    def insert_at_end(self, value):
        temp = Node(value)
        if self.start is None:  # Empty List
            self.start = temp
        else:  # else fo to the end of the list
            p = self.start
            while p.link is not None:
                p = p.link
            # At Last node
            p.link = temp

    def insert_after_node(self, node, data):
        p = self.start
        temp = Node(data)
        while p is not None:
            if p.value == node:
                temp.link = p.link
                p.link = temp
                break
            p = p.link
        else:
            print('\n', node, "is not present in the List ", '\n')
            return

    def insert_before_node(self, node, data):
        if self.start.value == node:  # if present at the first node
            self.insert_at_beginning(data)  # Callinf inser at the beginnig
            return

        p = self.start
        temp = Node(data)
        while p.link is not None:
            if p.link.value == node:
                temp.link = p.link
                p.link = temp
                break
            p = p.link
        else:
            print('\n', node, "is not found in the List", '\n')
            return

    def insert_at_position(self, pos, data):
        if pos == 1:  # At the beginning
            self.insert_at_beginning(data)
            return
        temp = Node(data)
        p = self.start
        i = 1
        while i < pos - 1 and p is not None:
            p = p.link
            i += 1

        if p is None:
            print('You can insert node only upto ', i)
        else:
            # Now reference variable is at Pos-1
            temp.link = p.link
            p.link = temp

    # ****************************** Deletion ********************************

    def delete_first_node(self):
        if self.start is None: # If Empty List: Deletion is not possible
            return
        # otherwise
        self.start = self.start.link

    def delete_last_node(self):
        # If list is Empty
        if self.start is None:
            print("The List is Empty")
            return
        # If List has only one Node
        if self.start.link is None:
            self.start = None
            return
        # Otherwise delete last node
        p = self.start
        while p.link.link is not None : # Go to second last node
            p = p.link
        p.link = None # Assign second last link to None; Last node is deleted

    # Module to delete a given node
    def delete_a_node(self, node):
        # if list is empty that is self.start will be None
        if self.start is None:
            print('The list is Empty:(')
            return

        # If first node has to be deleted
        if self.start.value == node:
            self.start = self.start.link  # Assign the start to the second node.
            return

        # If a node is present in between the Nodes
        p = self.start
        while p.link is not None:  # Traverse till the end
            if p.link.value == node:  # If the node is found
                p.link = p.link.link
                break  # Break the loop once deleted
            p = p.link  # node is not found move to next node

        # If traversed and the node is not found
        if p.link is None:
            print('{} is not found in the list'.format(node))

    # ******************************* Reversing a Linked list **********************
    def reverse_list(self):
        p = self.start
        prev = None
        while p is not None:
            next = p.link
            p.link = prev
            prev = p
            p = next
        self.start = prev

    # **************************** Sorting **********************************

    # ******************** Bubble Sort ***************************

    def bubble_sort_exdata(self):
        pass

    # ****************************** Display, Count *********************************
    def display_list(self):
        if self.start is None:
            print("The List is Empty")
            return  # Return the control back
        else:
            p = self.start  # Create a RV by aliasing
            print('\n' + "The List is: ")
            print('start', end='')
            while p is not None:
                print('-->', p.value, end=' ')
                p = p.link
            print('\n')

    def count_nodes(self):
        if self.start is None:
            print("The List is Empty and count is 0")
            return
        else:
            c = 0  # Counter variable is initialized to 0
            p = self.start
            while p is not None:
                c += 1  # Increment before going to next node
                p = p.link
            print("The Number of Nodes are: ", c)


slist = SingleLinkedList()  # Create single linked list object
slist.create_list()
print()

while True:
    print(('*' * 20) + '**  Menu  **' + ('*' * 20))
    print('\t\t1.Display the List')
    print('\t\t2.Insert at the Beginnig')
    print('\t\t3.Insert at the End')
    print('\t\t4.Insert after a node')
    print('\t\t5.Insert before a node')
    print('\t\t6.Insert at a Position')
    print('\t\t7.Delete First Node')
    print('\t\t8.Delete Last Node')
    print('\t\t9.Delete a given node')
    print('\t\t10.Reverse a list')
    print('\t\t11.Bubblesort Exchange data')
    print('\t\t12.Count Number of nodes')
    print('\t\t20.Quit')
    op = int(input('Enter your option: '))

    if op == 1:
        slist.display_list()
    elif op == 2:
        data = int(input('Enter a value to insert: '))
        slist.insert_at_beginning(data)
    elif op == 3:
        data = int(input('Enter a vale to insert: '))
        slist.insert_at_end(data)
    elif op == 4:
        node = int(input('Enter a node after which a new node to be inserted: '))
        temp_node = int(input('Enter new node value: '))
        slist.insert_after_node(node, temp_node)
    elif op == 5:
        node = int(input('Enter a node before which a new node to be inserted: '))
        temp_node = int(input('Enter new node value: '))
        slist.insert_before_node(node, temp_node)
    elif op == 6:
        pos = int(input('At what position?: '))
        value = int(input('Enter the Value'))
        slist.insert_at_position(pos, value)
    elif op == 7:
        slist.delete_first_node()
    elif op == 8:
        slist.delete_last_node()
    elif op == 9:
        slist.display_list()
        node = int(input('Enter a node to be deleted: '))
        slist.delete_a_node(node)
    elif op == 10:
        print('Original ', end='')
        slist.display_list()
        slist.reverse_list()
        print('Reversed ', end='')
        slist.display_list()
    elif op == 11:
        print('Original ', end='')
        slist.display_list()
        slist.bubble_sort_exdata()
        print('Sorted ', end='')
        slist.display_list()
    elif op == 12:
        slist.count_nodes()

    elif op == 20:
        exit(0)
