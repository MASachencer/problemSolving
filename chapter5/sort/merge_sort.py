def merge_sort(lyst):
    if len(lyst) > 1:
        mid = len(lyst) // 2
        front_half = lyst[:mid]
        rear_half = lyst[mid:]
        merge_sort(front_half)
        merge_sort(rear_half)
        i, j, k = 0, 0, 0
        while i < len(front_half) and j < len(rear_half):
            if front_half[i] < rear_half[j]:
                lyst[k] = front_half[i]
                i += 1
            else:
                lyst[k] = rear_half[j]
                j += 1
            k += 1
        while i < len(front_half):
            lyst[k] = front_half[i]
            i += 1
            k += 1
        while j < len(rear_half):
            lyst[k] = rear_half[j]
            j += 1
            k += 1
    return lyst


lyst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(merge_sort(lyst))
