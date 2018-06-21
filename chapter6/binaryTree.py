# from pythonds.trees.binaryTree import BinaryTree
import operator
from .stack import Stack
from .queue_ import Queue_


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if isinstance(newNode, BinaryTree):
            t = newNode
        else:
            t = BinaryTree(newNode)
        if self.leftChild is not None:
            t.left = self.leftChild
        self.leftChild = t

    def insertRight(self, newNode):
        if isinstance(newNode, BinaryTree):
            t = newNode
        else:
            t = BinaryTree(newNode)
        if self.rightChild is not None:
            t.right = self.rightChild
        self.rightChild = t

    def isLeaf(self):
        return (not self.leftChild) and (not self.rightChild)

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self,):
        return self.key

    # 前序遍历：递归
    # 首先访问根节点，然后递归地做左侧子树的前序遍历，
    # 随后是右侧子树的递归前序遍历。
    def preorder_recur(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder_recur()
        if self.rightChild:
            self.rightChild.preorder_recur()

    # 前序遍历：非递归，用栈实现，
    # push整棵树，当栈顶不为空时，弹出栈顶
    # 入栈先右后左
    def preorder(self):
        s = Stack()
        s.push(self)
        while not s.is_empty():
            t = s.pop()
            print(t.key)
            if t.rightChild:
                s.push(t.rightChild)
            if t.leftChild:
                s.push(t.leftChild)

    # 中序遍历：递归
    # 递归地对左子树进行一次遍历，访问根节点，
    # 最后递归遍历右子树。
    def inorder_recur(self):
        if self.leftChild:
            self.leftChild.inorder_recur()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder_recur()

    # 后序遍历：递归
    # 递归地对左子树和右子树进行后序遍历，
    # 然后访问根节点。
    def postorder_recur(self):
        if self.leftChild:
            self.leftChild.postorder_recur()
        if self.rightChild:
            self.rightChild.postorder_recur()
        print(self.key)

    # 层序遍历：用队列实现
    def level(self):
        q = Queue_()
        q.enqueue(self)
        while not q.is_empty():
            t = q.dequeue()
            print(t.key)
            if t.leftChild:
                q.enqueue(t.leftChild)
            if t.rightChild:
                q.enqueue(t.rightChild)

    def printexp(self):
        if self.leftChild:
            print('(', end=' ')
            self.leftChild.printexp()
        print(self.key, end=' ')
        if self.rightChild:
            self.rightChild.printexp()
            print(')', end=' ')

    def postordereval(self):
        opers = {'+': operator.add, '-': operator.sub,
                 '*': operator.mul, '/': operator.truediv}
        res1 = None
        res2 = None
        if self.leftChild:
            res1 = self.leftChild.postordereval()
        if self.rightChild:
            res2 = self.rightChild.postordereval()
        if res1 and res2:
            return opers[self.key](res1, res2)
        else:
            return self.key


def inorder(tree):
    if tree is not None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())


def printexp(tree):
    if tree.leftChild:
        print('(', end=' ')
        printexp(tree.getLeftChild())
    print(tree.getRootVal(), end=' ')
    if tree.rightChild:
        printexp(tree.getRightChild())
        print(')', end=' ')


def printexp_(tree):
    sVal = ""
    if tree:
        sVal = '( {printexp(tree.getLeftChild())}'
        sVal = '{sVal} {str(tree.getRootVal())}'
        sVal = '{sVal} {printexp(tree.getRightChild())} )'
    return sVal


def postordereval(tree):
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()


def height(tree):
    if tree is None:
        return -1
    else:
        return 1 + max(height(tree.leftChild), height(tree.rightChild))
