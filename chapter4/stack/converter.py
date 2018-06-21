import string
from .stack import Stack


def base_converter(dec_num, base):
    convert_str = string.hexdigits
    r_stack = Stack()
    while dec_num > 0:
        if dec_num < base:
            r_stack.push(convert_str[dec_num])
        else:
            r_stack.push(convert_str[dec_num % base])
        dec_num //= base
    res = ''
    while not r_stack.is_empty():
        res += str(r_stack.pop())
    return res.upper()


print(base_converter(30, 2))
print(base_converter(30, 8))
print(base_converter(30, 16))
