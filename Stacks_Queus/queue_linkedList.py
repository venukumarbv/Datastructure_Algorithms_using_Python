'''
Queue can be implemented using Double Ended Linked list
'''
class QueueEmpty(Exception):
    def __init__(self, msg):
        self.msg = msg

class Node:
    def __init__(self, value):
        self.info = value
        self.link = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def is_empty(self):
        return self.front == None

    def enqueue(self, value):
        temp = Node(value)
        if self.front is None:
            self.front = temp
        else:
            self.rear.link = temp
        self.rear = temp
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise QueueEmpty('THe Queue is Empty Exception')
        x = self.front.info
        self.front = self.front.link
        self.count -= 1
        return x

    def peek(self):
        if self.is_empty():
            raise QueueEmpty('THe Queue is Empty Exception')
        return self.front.info

    def size(self):
        return self.count

    def display(self):
        if self.is_empty():
            print("The Queue is Empty")
            return
        p = self.front
        while p is not None:
            print(p.info, end=' ')
            p = p.link
        print()

q = Queue()

while True:
    print(('*' * 20) + '**  Menu  **' + ('*' * 20))
    print('\t\t1.Enqueue')
    print('\t\t2.Deque')
    print('\t\t3.Peek')
    print('\t\t4.Size')
    print('\t\t5.Display')
    print('\t\t6.Quit')
    op = int(input("Enter Your Option "))

    if op == 1:
        value = int(input("Enter the value to be Enqueue: "))
        q.enqueue(value)
    elif op == 2:
        print("The Dequeued item is {}".format(q.dequeue()))
    elif op == 3:
        print("The top of the Queue {}".format(q.peek()))
    elif op == 4:
        print("The size of the stack is {}".format(q.size()))
    elif op == 5:
        q.display()
    elif op == 6:
        exit(0)
    else:
        print("Wrong Choice, please select from the given option")
    print()