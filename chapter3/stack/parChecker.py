from .stack import Stack


def matches(open, close):
    opens = '{[('
    closers = '}])'
    return opens.index(open) == closers.index(close)


def par_checker1(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index += 1
    return balanced and s.is_empty()


def par_checker2(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in '{[(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    return balanced and s.is_empty()


print(par_checker1('((()))'))
print(par_checker1('(()'))

print(par_checker2('{{([][])}()}'))
print(par_checker2('[{()]'))
