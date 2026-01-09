def max_num(a, b):
    return max(a, b)

print (max_num(5, 10))


def difference(a, b):
    if a - b >= 135:
        print('YES')
    else:
        print('NO')

print (difference(140, 2))


def season(num):
    if num == 12 or num == 1 or num == 2:
        print('Зима')
    elif num in range(3, 6):
        print('Весна')
    elif num in range(6, 9):
        print('Лето')
    elif num in range(9, 12):
        print('Осень')
    else:
        print('Введите цифру от 1 до 12')

season(12)


def biggest(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print('YES')
    else:
        print('NO')

biggest(11, 20, 30)

