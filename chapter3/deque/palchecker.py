from .deque import Deque


def palchecker(astr):
    char_d = Deque()
    still_eq = True
    for ch in astr:
        char_d.add_rear(ch)
    while char_d.size() > 1 and still_eq:
        first = char_d.remove_front()
        last = char_d.remove_rear()
        if first != last:
            still_eq = False
    return still_eq


print(palchecker('lsdkjfskf'))
print(palchecker('radar'))
