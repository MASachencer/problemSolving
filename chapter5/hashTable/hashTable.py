class HashTable:
    def __init__(self, size=8):
        self.slots = [None] * size
        self.value = [None] * size
        self.length = 0

    @property
    def _load_factor(self):
        return self.length / float(len(self.slots))

    def __len__(self):
        return self.length

    def __iter__(self):
        for slot in self.slots:
            if slot is not None:
                yield slot

    def __contains__(self, key):
        return self.get(key) is not None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def hash_func(self, key):
        l = len(self.slots)
        hash_value = abs(hash(key)) % l
        while self.slots[hash_value] is not None and \
                self.slots[hash_value] != key:
            hash_value = (hash_value + 1 + l) % l
        return hash_value

    def rehash(self):
        old_slots = self.slots
        old_value = self.value
        new_size = len(self.slots) * 2
        self.slots = [None] * new_size
        self.value = [None] * new_size
        self.length = 0
        for idx in range(len(old_slots)):
            if old_slots[idx] is not None:
                self.put(old_slots[idx], old_value[idx])

    def put(self, key, value):
        hash_value = self.hash_func(key)
        if self.slots[hash_value] == key:               # update
            self.value[hash_value] = value
        elif self.slots[hash_value] is None:            # add
            self.slots[hash_value] = key
            self.value[hash_value] = value
            self.length += 1
            if self._load_factor >= 0.8:
                self.rehash()

    def get(self, key):
        hash_value = self.hash_func(key)
        if self.slots[hash_value] == key:
            return self.value[hash_value]
        elif self.slots[hash_value] is None:
            return None
        return None

    def remove(self, key):
        hash_value = self.hash_func(key)
        if self.slots[hash_value] == key:
            self.slots[hash_value] = None
            self.value[hash_value] = None
            self.length -= 1
        elif self.slots[hash_value] is None:
            self.value[hash_value] = None
