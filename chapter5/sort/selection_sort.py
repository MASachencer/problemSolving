def selection_sort(lyst):
    for rear in range(len(lyst) - 1, 1, -1):
        max_idx = 0
        for front in range(rear + 1):
            if lyst[max_idx] < lyst[front]:
                max_idx = front
        if max_idx != rear:
            lyst[max_idx], lyst[rear] = lyst[rear], lyst[max_idx]
    return lyst


lyst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(selection_sort(lyst))
