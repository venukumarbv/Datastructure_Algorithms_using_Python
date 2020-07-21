class QueueError(Exception):
    def __init__(self, msg):
        self.msg = msg

class Node:
    def __init__(self, data, data_priority):
        self.info = data
        self.priority = data_priority
        self.link = None

class PriorityQueue:
    def __init__(self):
        self.front =None

    def is_empty(self):
        return self.front == None

    def enqueue(self, data, data_priority):
        temp = Node(data, data_priority)
        if self.is_empty() or data_priority < self.front.priority : # Insert at beginning
            temp.link = self.front
            self.front = temp
        else:
            p = self.front
            while p.link is not None and p.link.priority <= data_priority :
                p = p.link
            temp.link = p.link
            p.link = temp

    def dequeue(self):
        if self.is_empty():
            raise QueueError("The Queue is Empty Exception")
        x = self.front.info
        self.front = self.front.link
        return x

    def display(self):
        if self.is_empty():
            print("The queue is Empty")
            return
        p =self.front
        while p is not None:
            print('[', p.priority, '|', p.info, ']', end= '--> ')
            p = p.link
        print()

    def size(self):
        n = 0
        p = self.front
        while p is not None:
            n += 1
            p = p.link
        return n

q = PriorityQueue()

while True:
    print(('*' * 20) + '**  Menu  **' + ('*' * 20))
    print('\t\t1.Enqueue')
    print('\t\t2.Deque')
    print('\t\t3.Size')
    print('\t\t5.Display')
    print('\t\t6.Quit')
    op = int(input("Enter Your Option "))
    if op == 1:
        value = int(input("Enter the value to be Enqueue: "))
        priority = int(input("Enter the Priority of {}".format(value)))
        q.enqueue(value, priority)
    elif op == 2:
        print("The Dequeued item is {}".format(q.dequeue()))
    elif op == 3:
        print("The size of the stack is {}".format(q.size()))
    elif op == 5:
        q.display()
    elif op == 6:
        exit(0)
    else:
        print("Wrong Choice, please select from the given option")
    print()