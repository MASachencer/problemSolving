from hashTable import HashTable

class DictADT(HashTable):
    def __len__(self):
        return self._length

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __contains__(self, key):
        idx = self._hash_func(key)
        return self._slots[idx] is not None

    def __iter__(self):
        for key in self._keys:
            if key is not None:
                yield key

    def keys(self):
        self.__iter__()

    def values(self):
        for value in self._values:
            if value is not None:
                yield value

    def items(self):
        for i in range(len(self._keys)):
            if self._keys[i] is not None:
                yield self._keys[i], self._values[i]


def main_test():
    from random import randint
    d = DictADT()
    l = [randint(1, 50) for _ in range(50)]

    for i in l:
        d.put(i, i)

    for k, v in d.items():
        assert k == v

    assert sorted(list(d)) == sorted(list(d.values()))


if __name__ == '__main__':
    main_test()
