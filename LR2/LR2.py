def legendre_symbol(a, p):
    """
    Вычисляет символ Лежандра a/p
    """
    print("Вычисляем символ Лежандра для числа", a,"/",p)
    ls = pow(a, (p - 1) // 2, p)

    result = ls if ls != p - 1 else -1
    print("Символ Лежандра для числа", a/p, "равен", result)

    return result

def quadratic_residues_or_non(p):
    """
    Находит множество квадратичных вычетов/невычетов по модулю p
    """
    residues = []
    non_residues = []
    for a in range(1, p):
        print("------")
        print("Проверяем цифру", a)
        if legendre_symbol(a, p) == 1:
            residues.append(a)
            print("Цифра", a, "является квадратичным вычетом")
        else:
            non_residues.append(a)
            print("Цифра", a, "является квадратичным невычетом")
    return residues, non_residues

p = 7
residues, non_residues = quadratic_residues_or_non(p)
print("-------")
print("Множество квадратичных вычетов по модулю", p, ":", residues)
print("Множество квадратичных невычетов по модулю", p, ":", non_residues)