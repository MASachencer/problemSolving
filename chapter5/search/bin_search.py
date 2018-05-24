def bin_search(lyst, item):
    first = 0
    last = len(lyst) - 1
    found = False
    while first <= last and not found:
        mid_point = (first + last) // 2
        if item == lyst[mid_point]:
            found = True
        elif item < lyst[mid_point]:
            last = mid_point - 1
        elif item > lyst[mid_point]:
            first = mid_point + 1
    return found


def bin_search1(lyst, item):
    if len(lyst) == 0:
        return False
    else:
        mid_point = len(lyst) // 2
        if item == lyst[mid_point]:
            return True
        elif item < lyst[mid_point]:
            return bin_search1(lyst[:mid_point], item)
        elif item > lyst[mid_point]:
            return bin_search1(lyst[mid_point + 1:], item)


lyst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(bin_search(lyst, 3))
print(bin_search(lyst, 13))
print(bin_search1(lyst, 3))
print(bin_search1(lyst, 13))
