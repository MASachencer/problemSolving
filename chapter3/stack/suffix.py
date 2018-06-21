from .stack import Stack


def do_math(sym, op1, op2):
    if sym == '+':
        return op1 + op2
    elif sym == '-':
        return op1 - op2
    elif sym == '*':
        return op1 * op2
    elif sym == '/':
        return op1 / op2


def infix2suffix(infixexpr):
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    op_stack = Stack()
    suffix_list = []
    expr_list = infixexpr.split()
    for token in expr_list:
        if token.isdigit():
            suffix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                suffix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and \
                  (prec[op_stack.peek()] >= prec[token]):
                suffix_list.append(op_stack.pop())
            op_stack.push(token)
    while not op_stack.is_empty():
        suffix_list.append(op_stack.pop())
    return ' '.join(suffix_list)


def suffix_eval(suffixexpr):
    op_stack = Stack()
    expr_list = suffixexpr.split()
    for token in expr_list:
        if token.isdigit():
            op_stack.push(int(token))
        else:
            op2 = op_stack.pop()
            op1 = op_stack.pop()
            result = do_math(token, op1, op2)
            op_stack.push(result)
    return op_stack.pop()


def infix_eval(infixexpr):
    return suffix_eval(infix2suffix(infixexpr))


print(infix_eval('( 7 + 9 / 8 ) - ( 3 + 4 / 2 )'))
