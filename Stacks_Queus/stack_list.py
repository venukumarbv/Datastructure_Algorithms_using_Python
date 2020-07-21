class StackFull(Exception):
    def __init__(self,msg):
        self.msg = msg

class StackEmpty(Exception):
    def __init__(self,msg):
        self.msg = msg

class Stack:
    '''A Class to create and modify the Stck'''
    def __init__(self, max_size=10): # If the max_size is not provided assume size to be 10
        # create a list of items of max length
        self.items = [None] * max_size
        self.count = 0 # acts as both RV and counter

    def display(self):
        print("The Stack elements are: ")
        print(self.items)

    def length(self):
        print("The length of the stack is {}".format(self.count))

    def is_empty(self):
        return self.count == 0   # return True if empty

    def is_full(self):
        return self.count == len(self.items)    # return True if count value is equal to the max length

    def push(self, x):
        if self.is_full():
            raise StackFull("The Stack is Full cannot perform PUSH operation")

        self.items[self.count] = x
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise StackEmpty("The stack is Empty Cannot Perform POP operation")

        x = self.items[self.count - 1]
        self.items[self.count - 1] = None # Assign None to the popped Location
        self.count -= 1
        return x

    def peek(self):
        if self.is_empty():
            raise StackEmpty("The stack is Empty")
        return self.items[self.count - 1]

st = Stack(8)

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
        st.length()
    elif op == 5:
        st.display()
    elif op == 6:
        exit(0)
    else:
        print("Wrong Choice, please select from the given option")
    print()