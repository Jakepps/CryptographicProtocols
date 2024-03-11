# Примеры из задачи
is_irreducible_examples = [
    [1, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1],
]

irr_polynomials = [
    [1, 1, 1],  # x^2 + x + 1
    [1, 0, 1, 1],  # x^3 + x + 1
    [1, 0, 0, 1, 1],  # x^4 + x + 1
    [1, 0, 0, 1, 0, 1],  # x^5 + x^2 + 1
    [1, 0, 0, 0, 0, 1, 1],  # x^6 + x + 1
    [1, 0, 0, 0, 0, 0, 1, 1],  # x^7 + x + 1
    [1, 0, 0, 0, 1, 1, 1, 0, 1],  # x^8 + x^4 + x^3 + x^2 + 1
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],  # x^9 + x^4 + 1
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],  # x^10 + x^3 + 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # x^11 + x^2 + 1
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1],  # x^12 + x^6 + x^4 + x + 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],  # x^13 + x^4 + x^3 + x + 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],  # x^14 + x^10 + x^ 6 + x + 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],  # x^15 + x + 1
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],  # x^16 + x^12 + x^3 + x + 1
]


def is_irreduciblle(poly):
    # Полиномы степени 0 и 1 всегда неприводимы
    if len(poly) <= 2:
        return True
    elif len(poly) > 16:
        print("Максимальная степень до степени 16.")
        return False

    # Проверяем содержит ли irr_polynomials полином
    if poly in irr_polynomials:
        return True
    else:
        return False


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def gf2_poly_powmod(x, k, mod_poly):
    result = [1]  # многочлен степени 0
    while k > 0:
        if k & 1:
            result = gf2_poly_mod(gf2_poly_mul(result, x), mod_poly)
        x = gf2_poly_mod(gf2_poly_mul(x, x), mod_poly)
        k >>= 1
    return result

def gf2_poly_mod(poly, mod_poly):
    def degree(p):
        while p and p[-1] == 0:
            p.pop()  # Удаляем нулевые коэффициенты с конца
        return len(p) - 1

    dp = degree(poly)
    dm = degree(mod_poly)
    while dp >= dm:
        diff = [0]*(dp - dm) + mod_poly
        for i in range(len(poly)):
            poly[i] ^= diff[i]
        dp = degree(poly)
    return poly

def gf2_poly_mul(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, coeff_a in enumerate(a):
        for j, coeff_b in enumerate(b):
            result[i + j] ^= (coeff_a & coeff_b)
    return result

def is_primitive(poly):
    if not is_irreduciblle(poly):
        return False

    n = len(poly) - 1  # Степень многочлена
    order = 2 ** n - 1

    # Проверка, что x^(2^n - 1) ≡ 1 (mod poly)
    if gf2_poly_powmod([1, 0], order, poly) != [1]:
        return False

    # Проверка, что условие не выполняется для любого делителя 2^n - 1
    for q in prime_factors(order):
        if gf2_poly_powmod([1, 0], order // q, poly) == [1]:
            return False

    return True


for i, f in enumerate(is_irreducible_examples, start=1):
    print(f"Пример {i}.")
    print(f"Многочлен F(x): {f}")
    print("Проверка на примитивность:", is_primitive(f))
    print("\n")