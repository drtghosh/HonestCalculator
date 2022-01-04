# put your python code here
number_1 = float(input())
number_2 = float(input())
operation = input()

div_ops = ['/', 'mod', 'div']

if operation in div_ops:
    if number_2 == 0:
        print("Division by 0!")
    else:
        if operation == '/':
            print(number_1 / number_2)
        elif operation == 'mod':
            print(number_1 % number_2)
        else:
            print(number_1 // number_2)

if operation == '+':
    print(number_1 + number_2)
elif operation == '-':
    print(number_1 - number_2)
elif operation == '*':
    print(number_1 * number_2)
elif operation == 'pow':
    print(number_1 ** number_2)
