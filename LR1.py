from math import gcd


def euler_definition(n):
    count = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            count += 1
    return count

def euler_formula(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

number = 15
print("Функция Эйлера по определению для", number, ":", euler_definition(number))
print("Функция Эйлера с использованием формулы для", number, ":", euler_formula(number))
