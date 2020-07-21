class StackEmpty(Exception):
    def __init__(self, msg):
        self.msg = msg

class Node:
    def __init__(self, value):
        self.info = value
        self.link = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def size(self):
        if self.is_empty():
            print("The list is Empty")
            return 0
        count = 0
        p = self.top
        while p is not None:
            count += count
            p = p.link
        return count

    def push(self, value):
        temp = Node(value)
        temp.link = self.top
        self.top = temp

    def pop(self):
        if self.is_empty():
            raise StackEmpty("The Stack is Empty , Cannot Perform POP opration")
        popped = self.top.info
        self.top = self.top.link
        return popped

    def display(self):
        if self.is_empty():
            print("The list is Empty")
            return
        p = self.top
        while p is not None:
            print(p.info, end='')
            p = p.link

    def peek(self):
        if self.is_empty():
            raise StackEmpty("The Stack is Empty , Cannot Perform POP opration")
        return self.top.info

st = Stack()

while True:
    print(('*' * 20) + '**  Menu  **' + ('*' * 20))
    print('\t\t1.Push')
    print('\t\t2.Pop')
    print('\t\t3.Peek')
    print('\t\t4.Size')
    print('\t\t5.Display')
    print('\t\t6.Quit')
    op = int(input("Enter Your Option "))

    if op == 1:
        value = int(input("Enter the value to be Pushed: "))
        st.push(value)
    elif op == 2:
        print("The Popped Item is {}".format(st.pop()))
    elif op == 3:
        print("The top of the Stack is {}".format(st.peek()))
    elif op == 4:
        print("The size of the stack is {}".format(st.size()))
    elif op == 5:
        st.display()
    elif op == 6:
        exit(0)
    else:
        print("Wrong Choice, please select from the given option")
    print()