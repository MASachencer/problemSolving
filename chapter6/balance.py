# from pythonds.trees.balance import AVLTree
from .bst import TreeNode, BinarySearcheTree


class AVLTree(BinarySearcheTree):
    def _put(self, key, value, node):
        if key < node.key:
            if node.get_left():
                self._put(key, value, node.left)
            else:
                node.left = TreeNode(key, value)
                node.parent = node
                self.update_balance(node.left)
        else:
            if node.get_right():
                self._put(key, value, node.right)
            else:
                node.right = TreeNode(key, value)
                node.parent = node
                self.update_balance(node.right)

    def update_balance(self, node):
        if abs(node.balance_factor) > 1:
            self.reblance()
            return
        if node.parent:
            if node.is_leaf():
                node.parent.balance += 1
            elif node.is_right():
                node.parent.balance -= 1
            if node.parent.balance != 0:
                self.update_balance(node.parent)

    def rebalance(self, node):
        if node.balance_factor < 0:
            if node.right.balance_factor > 0:
                self.rotate_right(node.right)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left.balance_factor < 0:
                self.rotate_left(node.left)
                self.rotate_right(node)
            else:
                self.rotate_right(node)

    def rotate_left(self, rot_root):
        new_root = rot_root.right
        rot_root.right = new_root.left
        if new_root.left:
            new_root.left.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_left():
                rot_root.parent.left = new_root
            else:
                rot_root.parent.right = new_root
        new_root.left = rot_root
        rot_root.parent = new_root
        rot_root.balance_factor = rot_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(rot_root.balance_factor, 0)

    def rotate_right(self, rot_root):
        new_root = rot_root.left
        rot_root.left = new_root.right
        if new_root.right:
            new_root.right.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_right():
                rot_root.parent.right = new_root
            else:
                rot_root.parent.left = new_root
        new_root.right = rot_root
        rot_root.parent = new_root
        rot_root.balance_factor = rot_root.balance_factor + 1 - max(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + min(rot_root.balance_factor, 0)
