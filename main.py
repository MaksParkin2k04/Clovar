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

def z16():
    '''Все похожие на эти'''
    # Сама функция
    def F(n):
        if n == 1: return 1
        if n % 2 == 0: return n + F(n - 1)
        if n > 1 and n % 2 != 0: return 3 * F(n - 2)

    # Основная часть программы
    print(F(25))

    ''''''

    # Сама функция
    def F(n):
        if n > 25: return 2 * n * n * n + 1
        if n <= 25: return F(n + 2) + 2 * F(n + 3)

    k = 0

    # Перебираем диапазон
    for i in range(1, 1001):
        if F(i) % 11 == 0:
            k = k + 1

    print(k)
def z17():
    with open('17.txt') as f:
        n = [int(x) for x in f]
    mn = min(x for x in n if x % 21 == 0)
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

def z25_0():
    '''Назовём маской числа последовательность цифр, в которой также могут
встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной
длины; в том числе «*» может задавать и пустую последовательность.
Среди натуральных чисел, не превышающих 109
, найдите все числа,
соответствующие маске 12345?6?8 и делящиеся на 17 без остатка. В ответе
запишите в первом столбце таблицы все найденные числа в порядке
возрастания, а во втором столбце — соответствующие им частные от
деления на 17.
'''
    for a in range(10):
        for b in range(10):
            x =  int(f'12345{a}6{b}8')
            if x % 17 == 0:
                print(x,x//17)

def z25_2():
    '''На делители'''
    import math  # для квадратного корня sqrt
    divCount = 6  # нужное количество делителей
    for n in range(164700, 164752 + 1):
        divs = []  # чистим список делителей
        for d in range(1, round(math.sqrt(n))):  # перебор делителей
            if n % d == 0:
                divs.append(d)  # добавляем делитель в список
                if d != n // d:
                    divs.append(n // d)
                if len(divs) > divCount: break
        if len(divs) == divCount:
            divs.sort()
            print(divs)

def z25_3():
    '''Задание на четные делители'''
    divCount = 4  # нужное количество делителей
    for n in range(190201, 190280 + 1):
        divs = []  # чистим список делителей
        for d in range(1, n + 1):  # перебор делителей
            if n % d == 0 and d % 2 == 0:
                divs.append(d)  # добавляем делитель в список
                if len(divs) > divCount: break
        if len(divs) == divCount:
            divs.sort()
            divs.reverse()
            print(divs)

def z25_4():
    '''Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [394441; 394505],
     числа, имеющие максимальное количество различных делителей. Если таких чисел несколько, то найдите минимальное из них.
    Выведите количество делителей найденного числа и два наибольших делителя в порядке убывания.'''
    maxim = 0
    divsmax = []
    for n in range(394441, 394505 + 1):
        divs = [d for d in range(1, n + 1) if n % d == 0]
        if len(divs) > maxim:
            maxim = len(divs)
            divsmax = divs  # сохраняем делители для числа с макс кол-вом дел-ей
    divsmax.reverse()
    print(maxim, divsmax[0], divsmax[1])

def z25_5():
    '''Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [3532000; 3532160], простые числа.
Выведите все найденные простые числа в порядке убывания, слева от каждого числа выведите его номер по порядку.'''
    cn = 0  # для порядкового номера в самом отрезке
    count = 0
    for n in range(3532160, 3532000 - 1, -1):  # цикл с конца и с шагом (-1)
        flag = True
        cn += 1
        for d in range(2, n):  # перебор делителей, начиная с двух
            if n % d == 0:  # есть делитель помимо единицы и самого n
                flag = False  # число не простое
                break
        if flag == True:  # число простое
            count += 1
            print(count,cn, n)



if __name__ == '__main__':
    for n in range(190201, 190230 + 1):
        divs = []  # чистим список делителей
        for d in range(1, n + 1):  #
            if n % d == 0:
                divs = divs + [d]  # добавляем делитель в список
                if len(divs) > 4:
                    break
        if len(divs) == 4:
            divs.reverse()
            divs.sort()
            print(*divs)


