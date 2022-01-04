# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
operators = ['+', '-', '*', '/']
memory = 0


def perform_op(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b


def is_one_digit(v):
    return v.is_integer() and abs(v) < 10


def check(a, b, op):
    msg = ""
    if is_one_digit(a) and is_one_digit(b):
        msg += msg_6
    if (a == 1 or b == 1) and op == '*':
        msg += msg_7
    if (a == 0 or b == 0) and (op in '+-*'):
        msg += msg_8
    return msg


def calculate_operation(m=memory):
    while True:
        print(msg_0)
        # following variable calc should have the format: x operation y
        # for example: 2 + 3, 2 + g or 3.1 r 5
        calc = input()
        x, oper, y = calc.split()
        if x == 'M':
            x = m
        if y == 'M':
            y = m
        try:
            float(x) and float(y)
        except ValueError:
            print(msg_1)
        else:
            if oper in operators:
                x, y = float(x), float(y)
                message = check(x, y, oper)
                if message != "":
                    print(msg_9 + message)
                result = perform_op(x, y, oper)
                if result is not None:
                    print(result)
                    return result
                else:
                    print(msg_3)
            else:
                print(msg_2)


def print_msg(index):
    if index == 10:
        print(msg_10)
    if index == 11:
        print(msg_11)
    if index == 12:
        print(msg_12)


def to_memory(res, mem=memory):
    if is_one_digit(res):
        msg_index = 10
        while True:
            print_msg(msg_index)
            one_store = input()
            if one_store not in 'yn':
                continue
            elif one_store == 'y':
                if msg_index < 12:
                    msg_index += 1
                    continue
                else:
                    mem = res
                    return mem
            else:
                return mem
    else:
        mem = res
        return mem


new_result = calculate_operation()
while True:
    print(msg_4)
    store = input()
    if store not in 'yn':
        continue
    else:
        if store == 'y':
            memory = to_memory(new_result, memory)
        print(msg_5)
        while True:
            cont = input()
            if cont not in 'yn':
                break
            elif cont == 'y':
                new_result = calculate_operation(memory)
                break
            else:
                exit(0)
