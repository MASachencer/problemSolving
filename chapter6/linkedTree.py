from stack import Stack
from queue_ import Queue_


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.left} <-- {self.value} --> {self.right}'

    def __repr__(self):
        return self.__str__()


class Tree:
    def __init__(self, node):
        self.root = node

    def insert_left(self, node):
        self.root.left = node

    def insert_right(self, node):
        self.root.right = node

    def is_leaf(self):
        return (not self.left) and (not self.right)

    def get_left(self):
        return self.left.data

    def get_right(self):
        return self.right.data

    def get_root(self):
        return self.root.data

    # 前序遍历：递归
    # 首先访问根节点，然后递归地做左侧子树的前序遍历，
    # 随后是右侧子树的递归前序遍历。
    def preorder_recur(self):
        print(self.root.data)
        if self.left is not None:
            self.left.preorder_recur()
        if self.right is not None:
            self.right.preorder_recur()

    # 前序遍历：非递归，用栈实现，
    # push整棵树，当栈顶不为空时，弹出栈顶
    # 入栈先右后左
    def preorder(self):
        s = Stack()
        s.push(self.root)
        while not s.is_empty():
            t = s.pop()
            print(t.root.data)
            if t.right is not None:
                s.push(t.right)
            if t.left is not None:
                s.push(t.left)

    # 中序遍历：递归
    # 递归地对左子树进行一次遍历，访问根节点，
    # 最后递归遍历右子树。
    def inorder_recur(self):
        if self.left is not None:
            self.left.inorder_recur()
        print(self.root.data)
        if self.right is not None:
            self.right.inorder_recur()

    # 后序遍历：递归
    # 递归地对左子树和右子树进行后序遍历，
    # 然后访问根节点。
    def postorder_recur(self):
        if self.left is not None:
            self.left.postorder_recur()
        if self.right is not None:
            self.right.postorder_recur()
        print(self.root.data)

    # 层序遍历：用队列实现
    def level(self):
        q = Queue_()
        q.enqueue(self.root)
        while not q.is_empty():
            t = q.dequeue()
            print(t.root.data)
            if t.left is not None:
                q.enqueue(t.left)
            if t.right is not None:
                q.enqueue(t.right)
