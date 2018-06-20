class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def is_left(self):
        return self.parent and self.parent.left == self

    def is_right(self):
        return self.parent and self.parent.right == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not self.left and not self.right

    def has_any_child(self):
        return self.left or self.right

    def has_both_child(self):
        return self.left and self.right

    def replace(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def find_successor(self):
        succ = None
        if self.right:
            succ = self.right.find_min()
        else:
            if self.parent:
                if self.is_left():
                    succ = self.parent
                else:
                    self.parent.right = None
                    succ = self.parent.find_successor()
                    self.parent.right = self
        return succ

    def splice_out(self):
        if self.is_leaf():
            if self.is_left():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.has_any_child():
            if self.get_left():
                if self.is_left():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
            else:
                if self.is_left():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent

    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current

    def __iter__(self):
        if self:
            yield self.key
            if self.get_left():
                for elem in self.left:
                    yield elem
            if self.get_right():
                for elem in self.right:
                    yield elem

    def __str__(self):
        return f'{self.left} <-- {self.key} --> {self.right}'

    def __repr__(self):
        return self.__str__()

class BinarySearcheTrie:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def _put(self, key, value, current):
        if key < current.key:
            if current.get_left():
                self._put(key, value, current.left)
            else:
                current.left = TreeNode(key, value)
                current.left.parent = current
        else:
            if current.right:
                self._put(key, value, current.right)
            else:
                current.right = TreeNode(key, value)
                current.right.parent = current

    def __sititem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None

    def _get(self, key, current):
        if current.key == key:
            return current
        elif key < current.key:
            return self._get(key, current.left)
        elif key > current.key:
            return self._get(key, current.right)
        else:
            return None

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            node = self._get(key, self.root)
            if node:
                self.remove(node)
                self.size -= 1
            else:
                raise KeyError(f'Error, {key} not in tree.')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError(f'Error, {key} not in tree.')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, node):
        if node.is_leaf():
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.has_both_child():
            succ = node.find_successor()
            succ.splice_out()
            node.key = succ.key
            node.payload = succ.payload
        else:
            if node.get_left():
                if node.is_left():
                    node.left.parent = node.parent
                    node.parent.left = node.left
                elif node.is_right():
                    node.left.parent = node.parent
                    node.parent.right = node.left
                else:
                    node.replace(node.left.key, node.left.payload, node.left.left, node.left.right)
            else:
                if node.is_left():
                    node.right.parent = node.parent
                    node.parent.left = node.right
                elif node.is_right():
                    node.right.parent = node.parent
                    node.parent.right = node.right
                else:
                    node.replace(node.right.key, node.right.payload, node.right.left, node.right.right)
