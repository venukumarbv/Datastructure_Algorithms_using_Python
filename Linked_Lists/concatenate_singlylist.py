class Node:
    '''A Class to create a node object'''
    def __init__(self, value):
        self.info = value
        self.link = None

class SingleLinkedList:
    '''A Class to create and modify the Singly Linked List'''
    def __init__(self):
        self.start = None

    def insert_at_end(self, value):
        temp = Node(value)
        if self.start is None: # If Empty list
            self.start = temp
            return

        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def create_list(self):
        n = int(input("Enter the Number of nodes in the List: "))
        for i in range(n):
            value = int(input("Enter the Value of {} node: ".format(i+1)))
            self.insert_at_end(value)

    def display_list(self):
        if self.start is None:
            print("The List is Empty")
            return  # Return the control back
        else:
            p = self.start  # Create a RV by aliasing
            print('\n' + "The List is: ")
            print('start', end='')
            while p is not None:
                print('-->', p.info, end=' ')
                p = p.link
            print('-->end')

    def concatenate_list(self,list2):
        if self.start is None:
            self.start = list2.start
            return
        if list2.start is None:
            return
        p = self.start
        while p.link is not None:
            p = p.link
        p.link = list2.start



list1 = SingleLinkedList()
list2 = SingleLinkedList()

print("List 1")
list1.create_list()
print("List 2")
list2.create_list()

print("The List 1 is:")
list1.display_list()
print("The List 2 is:")
list2.display_list()

print("Concatenated List is ")
list1.concatenate_list(list2)
list1.display_list()