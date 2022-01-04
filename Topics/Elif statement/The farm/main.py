chicken_price = 23
goat_price = 678
pig_price = 1296
cow_price = 3848
sheep_price = 6769

money = int(input())


def print_style(num, item):
    if num > 1:
        print(f'{num} {item}s')
    else:
        print(f'1 {item}')


if money < chicken_price:
    print('None')
elif money < goat_price:
    chickens = money // chicken_price
    print_style(chickens, 'chicken')
elif money < pig_price:
    goats = money // goat_price
    print_style(goats, 'goat')
elif money < cow_price:
    pigs = money // pig_price
    print_style(pigs, 'pig')
elif money < sheep_price:
    cows = money // cow_price
    print_style(cows, 'cow')
else:
    sheep = money // sheep_price
    print(f'{sheep} sheep')
