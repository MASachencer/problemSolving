class HashTable:
    def __init__(self, size=8):
        self._keys = [None] * size
        self._values = [None] * size
        self._length = 0

    @property
    def _load_factor(self):
        return self._length / float(len(self._keys))

    def __len__(self):
        return self._length

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __contains__(self, key):
        idx = self._hash_func(key)
        return self._keys[idx] is not None

    def __iter__(self):
        for key in self._keys:
            if key is not None:
                yield key

    def _hash_func(self, key):
        l = len(self._keys)
        idx = abs(hash(key)) % l
        while self._keys[idx] is not None and \
                self._keys[idx] != key:
            idx = (idx + l + 1) % l
        return idx

    def put(self, key, value):
        idx = self._hash_func(key)
        if self._keys[idx] == key:               # update
            self._values[idx] = value
        elif self._keys[idx] is None:            # add
            self._keys[idx] = key
            self._values[idx] = value
            self._length += 1
            if self._load_factor >= 0.8:
                self._rehash()

    def get(self, key):
        idx = self._hash_func(key)
        if self._keys[idx] == key:
            return self._values[idx]
        elif self._keys[idx] is None:
            return None
        return None

    def remove(self, key):
        idx = self._hash_func(key)
        if self._keys[idx] == key:
            self._keys[idx] = None
            self._values[idx] = None
            self._length -= 1
        elif self._keys[idx] is None:
            self._values[idx] = None
        else:
            return -1

    def _rehash(self):
        old_slots = self._keys
        old_value = self._values
        new_size = len(self._keys) * 2
        self._keys = [None] * new_size
        self._values = [None] * new_size
        self._length = 0
        for idx in range(len(old_slots)):
            if old_slots[idx] is not None:
                self.put(old_slots[idx], old_value[idx])


def main_test():
    h = HashTable()
    h['a'] = 0
    h.put('b', 1)
    h['c'] = 2
    h.put('d', 3)

    assert len(h) == 4
    assert h['a'] == 0
    assert h.get('b') == 1
    assert h['o'] is None
    assert h['p'] is None
    h.remove('d')
    assert h['d'] is None

    for i in range(50):
        h.put(i, i)

    for i in range(50):
        assert h[i] == i


if __name__ == '__main__':
    main_test()
