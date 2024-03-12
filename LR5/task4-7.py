import math
from math import gcd
import random

#task 4 - Испытание квадратным корнем
# Числа для проверки
numbers = [23, 41, 15, 35, 561]

# Функция для проверки числа на простоту методом испытания квадратным корнем
def is_prime_sqrt_test(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Проведение проверки для каждого числа
print("Испытание квадратным корнем")
for n in numbers:
    print("Для n=", n, "результат равен:", is_prime_sqrt_test(n))


#task 5 - Тест Миллера-Рабина
    
def miller_rabin(n, k = 5):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Найти d, r такие, что d * 2^r = n - 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Провести k раундов тестирования
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Проведение теста Миллера-Рабина для каждого числа
print("\nТест Миллера-Рабина")
for n in numbers:
    print("Для числа n=",n,"результат равен:",miller_rabin(n))


#task 6 - Метод Ферма для разложения на множители
def fermat_factorization(n):
    x = math.ceil(math.sqrt(n))
    while True:
        y2 = x**2 - n
        y = math.sqrt(y2)
        if y.is_integer():
            return (int(x + y), int(x - y))
        x += 1

# Применяем метод Ферма к заданным числам
numbers = [483, 1207, 561, 1219]
print("\nМетод Ферма для разложения на множители")
for n in numbers:
    print("Для числа n=",n,"результат равен:",fermat_factorization(n))

#task 7 - Метод (p-1) Полларда
    
def pollard_p_minus_1(n, B=10):
    a = 2  # Начальное значение для a
    for j in range(2, B+1):
        a = pow(a, j, n)
    d = gcd(a-1, n)
    if 1 < d < n:  # Нашли нетривиальный делитель
        return d
    else:
        return None  # Делитель не найден или нужно увеличить B

# Применяем метод (p-1) Полларда к заданным числам
numbers = [483, 1207, 561, 1219]
print("\nМетод (p-1) Полларда")
for n in numbers:
    print("Для числа n=",n,"результат равен:",fermat_factorization(n))
