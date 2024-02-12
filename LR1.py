from math import gcd
import time
import random

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

random_numbers = [random.randint(10_000_001, 100_000_000) for _ in range(100)]

start_time = time.time()
for num in random_numbers:
    euler_definition(num)
end_time = time.time()
definition_time = end_time - start_time

start_time = time.time()
for num in random_numbers:
    euler_formula(num)
end_time = time.time()
formula_time = end_time - start_time

print("Время выполнения для функции Эйлера по определению:", definition_time)
print("Время выполнения для функции Эйлера с использованием формулы:", formula_time)