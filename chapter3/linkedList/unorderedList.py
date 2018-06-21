from .linkedNode import LinkedNode


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        found = False
        current = self.head
        while current is not None and not False:
            if current.get_data == item:
                found = True
            else:
                current = current.get_next()
        return found

    def add(self, item):
        temp = LinkedNode(item)
        temp.set_next(self.head)
        self.head = temp

    def remove(self, item):
        found = False
        previous = None
        current = self.head
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head == current.get_next()
        else:
            previous.set_next(current.get_next())
