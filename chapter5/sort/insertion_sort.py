def insertion_sort(lyst):
    for i in range(1, len(lyst)):
        idx = i
        while idx > 0 and lyst[idx - 1] > lyst[idx]:
            lyst[idx - 1], lyst[idx] = lyst[idx], lyst[idx - 1]
            idx -= 1
    return lyst


lyst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(insertion_sort(lyst))
