x = float(input())
y = float(input())
if x > 0:
    if y > 0:
        print('I')
    elif y < 0:
        print('IV')
    else:
        print("One of the coordinates is equal to zero!")
elif x < 0:
    if y > 0:
        print('II')
    elif y < 0:
        print('III')
    else:
        print("One of the coordinates is equal to zero!")
else:
    if y == 0:
        print("It's the origin!")
    else:
        print("One of the coordinates is equal to zero!")
