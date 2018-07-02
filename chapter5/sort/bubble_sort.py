def bubble_sort(lyst):
    for rear in range(len(lyst) - 1, 0, -1):
        for front in range(rear):
            if lyst[front] > lyst[front + 1]:
                lyst[front], lyst[front + 1] = lyst[front + 1], lyst[front]
    return lyst

 
def short_bubble_sort(lyst):
    swaped = True
    rear = len(lyst) - 1
    while rear > 0 and swaped:
        swaped = False
        for front in range(rear):
            if lyst[front] > lyst[front + 1]:
                swaped = True
                lyst[front], lyst[front + 1] = lyst[front + 1], lyst[front]
        rear -= 1
    return lyst


# lyst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
lyst = [3, 2, 1]
lyst1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(bubble_sort(lyst))
print(short_bubble_sort(lyst1))
