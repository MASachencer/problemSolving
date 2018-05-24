def bubble_sort(lyst):
    for length in range(len(lyst) - 1, 0, -1):
        for item in range(length):
            if lyst[item] > lyst[item + 1]:
                lyst[item], lyst[item + 1] = lyst[item + 1], lyst[item]
    return lyst


def short_bubble_sort(lyst):
    swaped = True
    length = len(lyst) - 1
    while length > 0 and swaped:
        swaped = False
        for item in range(length):
            if lyst[item] > lyst[item + 1]:
                swaped = True
                lyst[item], lyst[item + 1] = lyst[item + 1], lyst[item]
        length -= 1
    return lyst


# lyst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
lyst = [3, 2, 1]
lyst1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(bubble_sort(lyst))
print(short_bubble_sort(lyst1))
