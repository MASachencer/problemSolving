class MaxHeap:
    def __init__(self):
        self._items = []
        self._count = 0

    def __len__(self):
        return self._count

    def _perc_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self._items[idx] > self._items[parent]:
                self._items[idx], self._items[parent] = self._items[parent], self._items[idx]
            idx = parent

    def add(self, item):
        self._items.append(item)
        self._count += 1
        self._sift_up(self._count-1)

    def _max_child(self, idx):
        left, right = idx * 2 + 1, idx * 2 + 2
        if left > self._count - 1:
            return left
        else:
            if self._items[left] > self._items[right]:
                return left
            else:
                return right
            
    def _perce_down(self, idx):
        while (idx * 2 + 1) < self._count - 1:
            mc = self._max_child(idx)
            if self._items[idx] < self._items[mc]:
                self._items[idx], self._items[mc] = self._items[mc], self._items[idx]
            idx = mc


    def pop_max(self):
        self._items[0], self._items[self._count-1] = self._items[self._count-1], self._items[0]
        self._count -= 1
        item = self._items.pop()
        self._sift_down(0)
        return item

class MinHeap:
    def __init__(self):
        self._items = []
        self._count = 0

    def __len__(self):
        return self._count

    def _perc_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self._items[idx] < self._items[parent]:
                self._items[idx], self._items[parent] = self._items[parent], self._items[idx]
            idx = parent

    def add(self, item):
        self._items.append(item)
        self._count += 1
        self._sift_up(self._count-1)

    def _min_child(self, idx):
        left, right = idx * 2 + 1, idx * 2 + 2
        if left > self._count - 1:
            return left
        else:
            if self._items[left] < self._items[right]:
                return left
            else:
                return right
            
    def _perce_down(self, idx):
        while (idx * 2 + 1) < self._count - 1:
            mc = self._max_child(idx)
            if self._items[idx] > self._items[mc]:
                self._items[idx], self._items[mc] = self._items[mc], self._items[idx]
            idx = mc


    def pop_max(self):
        self._items[0], self._items[self._count-1] = self._items[self._count-1], self._items[0]
        self._count -= 1
        item = self._items.pop()
        self._sift_down(0)
        return item
