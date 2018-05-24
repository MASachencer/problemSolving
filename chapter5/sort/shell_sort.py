def gap_insertion_sort(lyst, start, gap):
    for i in range(start, len(lyst), gap):
        idx = i
        while idx > start and lyst[idx - gap] > lyst[idx]:
            lyst[idx - gap], lyst[idx] = lyst[idx], lyst[idx - gap]
            idx -= gap


def shell_sort(lyst):
    list_count = len(lyst) // 2
    while list_count > 0:
        for start in range(list_count):
            gap_insertion_sort(lyst, start, list_count)
        print(f'After increments of size {list_count} The list is {lyst}')
        list_count //= 2
    return lyst


lyst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(shell_sort(lyst))
