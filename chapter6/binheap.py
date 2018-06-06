# from pythonds.trees.binheap import BinHeap


class BinHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    def perc_up(self, idx):
        while idx // 2 > 0:
            if self.heaplist[idx] < self.heaplist[idx // 2]:
                self.heaplist[idx], self.heaplist[idx // 2] = \
                    self.heaplist[idx // 2], self.heaplist[idx]
            idx //= 2

    def insert(self, item):
        self.heaplist.append(item)
        self.currentSize += 1
        self.perc_up(self.currentSize)

    def min_child(self, idx):
        if (idx * 2 + 1 > self.currentSize) or \
            (self.currentSize[idx * 2] <
                self.currentSize[idx * 2 + 1]):
            return idx * 2
        else:
            return idx * 2 + 1

    def perc_down(self, idx):
        while (idx * 2) <= self.currentSize:
            mc = self.min_child(idx)
            if self.heaplist[idx] > self.heaplist[mc]:
                self.heaplist[idx], self.heaplist[mc] = \
                    self.heaplist[mc], self.heaplist[idx]
            idx = mc

    def del_min(self):
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist.pop()
        self.currentSize -= 1
        self.perc_down(1)
        return retval

    def build_heap(self, lis):
        idx = len(lis) // 2
        self.currentSize = len(lis)
        self.heaplist = [0] + lis[:]
        while idx > 0:
            self.perc_down(idx)
            idx -= 1
