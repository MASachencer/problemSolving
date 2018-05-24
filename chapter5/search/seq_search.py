def seq_search(lyst, item):
    pos = 0
    found = False
    while pos < len(lyst) and not found:
        if lyst[pos] == item:
            found = True
        else:
            pos += 1
    return found


def ord_seq_search(lyst, item):
    pos = 0
    found = False
    stop = False
    while pos < len(lyst) and not found and not stop:
        if lyst[pos] == item:
            found = True
        else:
            if lyst[pos] > item:
                stop = True
            else:
                pos += 1
    return found


lyst = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(seq_search(lyst, 3))
print(seq_search(lyst, 13))
lyst1 = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(ord_seq_search(lyst1, 3))
print(ord_seq_search(lyst1, 13))
