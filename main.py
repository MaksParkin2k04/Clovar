def z2():
    print('x y z w')
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                for w in 0, 1:
                    F = not (x <= z) or (y == w) or not (y)
                    if not (F):
                        print(x, z, y, w)
'''Подбираем print по таблице'''

def z5():
    for N in range(516):
        b = f'{N:b}'
        if N % 2 == 0:
            b +='10'
        else:
            b = '1' + b +'01'
        if int(b,2) > 516:
            print(N)
            break
def z6():
    for x in range(10000):
        s = x
        s = (s - 10) // 7
        n = 1
        while s > 0:
            n = n * 2
            s = s - n
        if n == 8:
            print(x)
            break

def z8():
    '''позже'''

def z12():
    s ='8'*86
    while '1111' in s or '8888' in s:
        if '1111' in s:
            s = s.replace('1111','8', 1)
        if '8888' in s:
            s = s.replace('8888', '11', 1)
    print(s)

def z14():
    x = 3 * 16 ** 2018 - 2 * 8 ** 1024 - 3 * 4 ** 1100 - 2 ** 1050 - 2022
    k = 0
    # в получившемся числе рассматриваем каждую цифру в 4-й системе сч.
    while x:
        if x % 4 == 3:  # если цифра = 3, то считаем ее
            k += 1
        x //= 4  # убираем разряд числа в 4-й системе сч.
    print(k)

def z15():
    for A in range(1, 70):
        OK = 1
        for x in range(1, 1000):
            OK *= ((x % 3 == 0) <= (not (x % 5 == 0))) or (x + A >= 70)
        if OK:
            print(A)


if __name__ == '__main__':
    z15()