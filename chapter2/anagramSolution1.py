def anagram_solution1(s1, s2):
    alist = list(s2)
    index1 = 0
    still_ok = True
    while index1 < len(s1) and still_ok:
        index2 = 0
        found = False
        while index2 < len(alist) and not found:
            if s1[index1] == alist[index2]:
                found = True
            else:
                index2 += 1
        if found:
            alist[index2] = None
        else:
            still_ok = False
        index1 += 1
    return still_ok


print(anagram_solution1('abcd', 'dcba'))
