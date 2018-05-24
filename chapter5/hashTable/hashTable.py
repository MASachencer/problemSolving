class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def hash_func(self, key, size):
        return key % size

    def rehash(self, old, size):
        return (old + 1) % size

    def put(self, key, data):
        hash_value = self.hash_func(key, len(self.slots))
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        elif self.slots[hash_value] == key:
            self.data[hash_value] = data
        else:
            next_slot = self.rehash(hash_value, len(self.slots))
            while self.slots[next_slot] is not None and \
                    self.slots[next_slot] != key:
                next_slot = self.rehash(next_slot, len(self.slots))
            if self.slots[next_slot] is None:
                self.slots[next_slot] = key
                self.data[next_slot] = data
            else:
                self.data[next_slot] = data

    def get(self, key):
        start_slot = self.hash_func(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data
