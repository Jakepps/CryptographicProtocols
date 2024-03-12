def legendre_symbol(a, p):
    """
    Вычисляет символ Лежандра a/p
    """
    ls = pow(a, (p - 1) // 2, p)
    return ls if ls != p - 1 else -1

def inverse_mod(a, m):
    """
    Нахождение обратного элемента для 'a' по модулю 'm'
    """
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m = a % m
        a = m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def quadratic_residue_modulo(d, m):
    """
    Решение квадратичного сравнения x^2 ≡ d (mod m)
    """
    solutions = []
    if legendre_symbol(d, m) == -1:
        return solutions  # нет решений
    for x in range(m):
        if (x*x - d) % m == 0:
            solutions.append(x)
    return solutions

# Примеры использования:
d = 8
m = 14
print(f"Решения x^2 ≡ {d} (mod {m}): {quadratic_residue_modulo(d, m)}")

d = 4
m = 21
print(f"Решения x^2 ≡ {d} (mod {m}): {quadratic_residue_modulo(d, m)}")

d = 8
m = 23
print(f"Решения x^2 ≡ {d} (mod {m}): {quadratic_residue_modulo(d, m)}")