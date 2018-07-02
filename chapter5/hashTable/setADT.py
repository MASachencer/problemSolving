from hashTable import HashTable


class SetADT(HashTable):
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

    def put(self, key):
        return super(SetADT, self).put(key, value=True)

    def __and__(self, other):
        if isinstance(other, SetADT):
            temp = SetADT()
            for element in self:
                if element in other:
                    temp.put(element)
            return temp
        else:
            raise TypeError()

    def __sub__(self, other):
        if isinstance(other, SetADT):
            temp = SetADT()
            for element in self:
                if element not in other:
                    temp.put(element)
            return temp
        else:
            raise TypeError()

    def __or__(self, other):
        if isinstance(other, SetADT):
            temp = SetADT()
            for element in self:
                temp.put(element)
            for element in other:
                temp.put(element)
            return temp
        else:
            raise TypeError

    def __xor__(self, other):
        if isinstance(other, SetADT):
            union = self.__or__(other)
            intersection = self.__and__(other)
            temp = union.__sub__(intersection)
            return temp
        else:
            raise TypeError()


def main_test():
    a = SetADT()
    b = SetADT()
    a.put(0)
    a.put(1)
    a.put(2)
    b.put(2)
    b.put(3)
    b.put(4)

    assert 0 in a
    assert 4 in b

    assert sorted(list(a & b)) == [2]
    assert sorted(list(a - b)) == [0, 1]
    assert sorted(list(a | b)) == [0, 1, 2, 3, 4]


if __name__ == '__main__':
    main_test()
