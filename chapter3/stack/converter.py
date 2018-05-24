import string
from stack import Stack


def decimal2binary(dec_num):
    rem_stack = Stack()
    while dec_num > 0:
        rem = dec_num % 2
        rem_stack.push(rem)
        dec_num //= 2
    bin_str = ''
    while not rem_stack.is_empty():
        bin_str += str(rem_stack.pop())
    return bin_str


def decimal2octal(dec_num):
    rem_stack = Stack()
    while dec_num > 0:
        rem = dec_num % 8
        rem_stack.push(rem)
        dec_num //= 8
    oct_str = ''
    while not rem_stack.is_empty():
        oct_str += str(rem_stack.pop())
    return oct_str


def base_converter(dec_num, base):
    rem_stack = Stack()
    while dec_num > 0:
        rem = dec_num % base
        rem_stack.push(rem)
        dec_num //= base
    new_str = ''
    while not rem_stack.is_empty():
        new_str += string.hexdigits[rem_stack.pop()]
    return new_str.upper()


print(decimal2binary(42))
print(decimal2octal(42))
print(base_converter(30, 2))
print(base_converter(30, 8))
print(base_converter(30, 16))
