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
def z17():
    with open('z17.txt') as f:
        n = [int(x) for x in f]
    mn = min(x for x in n if x % 17 == 0)
    sums = []
    for a, b in zip(n, n[1:]):
        if a % mn == 0 or b% mn == 0:
            sums.append(a+b)
    print((len(sums), max(sums)))


def z22():
    for x in range(10000000):
        s = x
        P = 10
        Q = 8
        K1 = 0
        K2 = 0
        while s <= 100:
            s = s + P
            K1 = K1 + 1
        while s >= Q:
            s = s - Q
            K2 = K2 + 1
        K1 += s
        K2 += s
        if K1 == 10 and K2 == 19:
            print(x)
            break


def z24():
    f = open('z24.txt')
    n = f.read()
    n = n.replace('AB', 'x')
    n = n.replace('AC', 'x')
    k=0
    m=0
    for i in range(len(n)):
        if n[i]=='x':
            k+=1
            m = max(m,k)
        else:
            k=0
    print(m)

def z25():
    for a in range(10):
        for b in range(10):
            x =  int(f'12345{a}6{b}8')
            if x % 17 == 0:
                print(x,x//17)

if __name__ == '__main__':
    z25()