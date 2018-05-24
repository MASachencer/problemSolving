import string


def base_converter(dec_num, base):
    convert_str = string.hexdigits.upper()
    if dec_num < base:
        return convert_str[dec_num]
    else:
        return base_converter(dec_num // base, base) + \
            convert_str[dec_num % base]


print(base_converter(30, 2))
print(base_converter(30, 8))
print(base_converter(30, 16))
