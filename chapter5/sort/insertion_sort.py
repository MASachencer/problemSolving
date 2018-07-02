def insertion_sort(lyst):
    for front in range(1, len(lyst)):
        rear = front
        while rear > 0 and lyst[rear - 1] > lyst[rear]:
            lyst[rear - 1], lyst[rear] = lyst[rear], lyst[rear - 1]
            rear -= 1
    return lyst


lyst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(insertion_sort(lyst))
