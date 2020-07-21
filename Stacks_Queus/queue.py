class QueueEmpty(Exception):
    def __init__(self, msg):
        self.msg = msg


class Queue:
    def __init__(self, max_size = 10):
        self.items = [None] * max_size
        self.front = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def enqueue(self, value):
        if self.count == len(self.items):
            self.resize(2 * len(self.items)) # function call
        i = (self.front + self.count) % len(self.items)
        self.items[i] = value
        self.count += 1

    def resize(self, new_size):
        old_list = self.items
        self.items = [None] * new_size
        i = self.front
        for c in range(self.count):
            self.items[c] = old_list[i]
            i = (i + 1) % len(old_list)
        self.front = 0

    def dequeue(self):
        if self.is_empty():
            raise QueueEmpty("The Queue is Empty cannot perform dequeue operation")

        x = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % len(self.items)
        self.count -= 1
        return x

    def peek(self):
        if self.is_empty():
            raise QueueEmpty("The Queue is Empty")

        return self.items[self.front]

    def display(self):
        print(self.items)

q = Queue(4)

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