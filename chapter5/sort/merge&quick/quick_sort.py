def partition(lyst, first, last):
    front = first + 1
    rear = last
    while True:
        while front <= rear and lyst[front] <= lyst[first]:
            front += 1
        while front <= rear and lyst[rear] >= lyst[first]:
            rear -= 1
        if front > rear:
            break
        else:
            lyst[front], lyst[rear] = lyst[rear], lyst[front]
    lyst[first], lyst[rear] = lyst[rear], lyst[first]
    return rear


def quick_sort_helper(lyst, first, last):
    if first < last:
        pivot = partition(lyst, first, last)
        quick_sort_helper(lyst, first, pivot)
        quick_sort_helper(lyst, pivot + 1, last)


def quick_sort(lyst):
    quick_sort_helper(lyst, 0, len(lyst) - 1)


lyst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(lyst)
print(lyst)
