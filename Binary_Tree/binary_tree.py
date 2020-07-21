from collections import deque

class Node:
    '''A class to define the Node attributes'''
    def __init__(self, value):
        self.lchild = None  # A link to left child
        self.info = value   # value of the node
        self.rchild = None  # A link to right child


class BinaryTree:
    '''A class to create a binary tree'''
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def createTree(self):
        self.root = Node('P')
        self.root.lchild = Node('Q')
        self.root.lchild.lchild = Node('A')
        self.root.lchild.rchild = Node('B')
        self.root.rchild = Node('R')
        self.root.rchild.rchild = Node('X')

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, p):
        if p is None:
            return
        self._inorder(p.lchild)
        print(p.info, " ",end='')
        self._inorder(p.rchild)

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, p):
        if p is None:
            return
        print(p.info, " ", end='')
        self._preorder(p.lchild)
        self._preorder(p.rchild)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, p):
        if p is None:
            return
        self._postorder(p.lchild)
        self._postorder(p.rchild)
        print(p.info, " ", end='')

    def levelOrder(self):
        if self.root is None:
            print("Tree is Empty ")
            return
        qu = deque()
        qu.append(self.root)

        while len(qu) != 0:
            p = qu.popleft()
            print(p.info, end='  ')
            if p.lchild is not None:
                qu.append(p.lchild)
            if p.rchild is not None:
                qu.append(p.rchild)

    def height(self):
        return self._height(self.root)

    def _height(self, p):
        if p is None:
            return 0
        hL = self._height(p.lchild)
        hR = self._height(p.rchild)

        if hL > hR:
            return 1 + hL
        else:
            return 1 + hR

bt = BinaryTree()

bt.createTree()
print("Level order Traversal: ")
bt.levelOrder()
print()
print("Postorder Traversal: ")
bt.postorder()
print()
print('Inorder Traversal: ')
bt.inorder()
print()
print('Preorder Travesal: ')
bt.preorder()
print()
print("Height is {} ".format(bt.height()))
