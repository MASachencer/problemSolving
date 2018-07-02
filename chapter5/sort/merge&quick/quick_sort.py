def partition(lyst, first, last):
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and lyst[left_mark] <= lyst[first]:
            left_mark += 1
        while lyst[right_mark] >= lyst[first] and right_mark >= left_mark:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            lyst[left_mark], lyst[right_mark] = lyst[right_mark], lyst[left_mark]
    lyst[first], lyst[right_mark] = lyst[right_mark], lyst[first]
    return right_mark


def quick_sort_helper(lyst, first, last):
    if first < last:
        splitpoint = partition(lyst, first, last)
        quick_sort_helper(lyst, first, splitpoint - 1)
        quick_sort_helper(lyst, splitpoint + 1, last)


def quick_sort(lyst):
    quick_sort_helper(lyst, 0, len(lyst) - 1)


lyst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(lyst)
print(lyst)
