class Node:
    def __init__(self, value):
        self.info = value  # Node Value
        self.link = None  # Node Link , initially it must be None [Info][link-->None]


class SingleLinkedList:

    # ******************************* Creating a list ******************
    def __init__(self):
        self.start = None  # A reference to the beginning of the Node

    def create_list(self):
        # Creating a new List
        n = int(input('Enter Number of Nodes: '))
        if n == 0:
            return

        for i in range(n):
            data = int(input('Enter the data to be inserted: '))
            self.insert_at_end(data)

    # ******************* Insertion *******************************

    def insert_at_beginning(self, value):
        # Create a Node
        temp = Node(value)

        # If there is no nodes assign self.start to temp
        if self.start is None:
            self.start = temp
            return
        else:  # else first create link to the exist list using temp.link = self.start, later self.start = temp
            temp.link = self.start
            self.start = temp
            return

    def insert_at_end(self, value):
        # create a Node
        temp = Node(value)

        # if ther is no nodes assign self.start to temp
        if self.start is None:
            self.start = temp  # Assign the link to the temp node
            return
        else:
            p = self.start  # Initialise  the reference to the beginning
            while p.link is not None:  # Move to the Last node by checking the condition
                p = p.link  # Move to Next node for every iteration
            p.link = temp  # Once reached the last node assign the link of the last node to the temp node

    def insert_after_node(self, node, value):
        temp = Node(value)  # Create a temporary node ready
        p = self.start  # Intialise a reference equal to start
        while p is not None:  # Traverse all/untill reaches the required 'node'
            if p.info == node:  # If the node matches assign the links of temp node
                temp.link = p.link
                p.link = temp
                break  # Once the link is set break out of the While loop
            p = p.link  # If node not found move to next node

        if p is None:  # If the reference has traversed all the nodes and didn't find the required node :print not Found
            print(node, 'is not present in the list')
            return

    def insert_before_node(self, node, value):

        if self.start.info == node:  # if present at the first node
            slist.insert_at_beginning(value)  # Callinf inser at the beginnig
            return

        temp = Node(value)
        p = self.start  # Initialise the reference to the start
        while p.link is not None:  # Traverse all the link untill you find the required node
            if p.link.info == node:  # if node is found , p is referring to the previous node now
                temp.link = p.link
                p.link = temp
                break
            p = p.link

        if p.link is None:
            print(node, 'is not found in the list :( ')
            return

    def insert_at_position(self, pos, value):
        # If position is 1: Insert at the beginning
        if pos == 1:
            self.insert_at_beginning(value)
            return
        # If pos is not 1
        temp = Node(value)  # Create a Node
        p = self.start  # Initialize a reference
        i = 1  # Initialize a counting variable

        while i < pos - 1 and p is not None:  # Loop until the position before the required position is reached
            p = p.link  # Move to Next node
            i += 1  # Increment the count ; When it reaches the position-1 Come out of the loop

        if p is None:
            print('You can insert node only upto ', i)
        else:
            # Now reference variable is at Pos-1
            temp.link = p.link
            p.link = temp

    # ****************************** Deletion ********************************

    def delete_first_node(self):
        # If the list is empty self.start will be none
        if self.start is None:
            print('The list is empty ')
            return
        # Else
        self.start = self.start.link # Connect to the second node

    def delete_last_node(self):
        # If the list is empty self.start will be none
        if self.start is None:
            print('The list is empty ')
            return

        # If has only one node
        if self.start.link is None:
            self.start = None
            return

        # Move to last-1 position
        p = self.start
        while p.link.link is not None: # checking last node p.link.link is None means reference is at  ==> last-1 node
            p = p.link
        p.link = None # Assign last-1 node to None so that Last node will be deleted

    # Module to delete a given node
    def delete_a_node(self,node):
        # if list is empty that is self.start will be None
        if self.start is None:
            print('The list is Empty:(')
            return

        # If first node has to be deleted
        if self.start.info == node:
            self.start = self.start.link # Assign the start to the second node.
            return

        # If a node is present in between the Nodes
        p = self.start
        while p.link is not None: # Traverse till the end
            if p.link.info == node: # If the node is found
                p.link = p.link.link
                break # Break the loop once deleted
            p = p.link # node is not found move to next node

        # If traversed and the node is not found
        if p.link is None:
            print('{} is not found in the list'.format(node))

    # ******************************* Reversing a Linked list **********************

    def reverse_list(self):
        # We need 3 reference variable say : prev, next and p
        # ** Initialize prev to None and p to self.start
        # Traverse through the list till p is not None
        # 1. Initialize next to p.link
        # 2. Initialize p.link to prev
        # 3. set prev to p
        # 4. Set p to next  ; Repeat 1,2,3,4 unitl p becomes None and prev is pointing to last node
        #    Outside the loop  which means p is none; traversed all the nodes ; only prev is available
        # 5. Assign self.start to prev

        # **
        prev = None
        p = self.start
        while p is not None:
            next = p.link
            p.link = prev
            prev = p
            p = next
        self.start = prev

    # **************************** Sorting **********************************

        #******************** Bubble Sort ***************************

    def bubble_sort_exdata(self):
        # We need three reference variable p, q and end
        # Initialize end to None
        # Sorting should stop when end variable reaches second node self.start.link >> Outside While Loop
        # Inner While loop to check whether p.link is end or not . If not end repeat the loop >> Inner While loop
            # 1. Assign q to next node of p ; that is q = p.link
            # check p > q ; if yes excahne the value p.info,q.info = q.info, p.info else move p to next node
            # Move p to next node p = pilink
        #When p.link is end assign end = p

        end = None
        while end != self.start.link:
            p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.info, q.info = q.info, p.info
                p = p.link
            end = p




    # ****************************** Display *********************************
    def display_list(self):
        # If the self.start is None means there are no Nodes hence the link is empty
        if self.start is None:
            print('List is Empty')
            return
        else:  # If there exist some Nodes
            print('List is ')
            p = self.start  # Start from the Beginning
            print('Start-->',end='')
            while p is not None:
                print(p.info, "---> ", end='')  # Print its value/info and go to next Node
                p = p.link  # Go to Next Node
            print('None')
        print()



slist = SingleLinkedList()
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
        print('Original ',end='')
        slist.display_list()
        slist.reverse_list()
        print('Reversed ',end='')
        slist.display_list()
    elif op == 11:
        print('Original ', end='')
        slist.display_list()
        slist.bubble_sort_exdata()
        print('Sorted ', end='')
        slist.display_list()

    elif op == 20:
        exit(0)
