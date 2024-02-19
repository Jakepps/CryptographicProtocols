def legendre_symbol(a, p):
    """
    Вычисляет символ Лежандра (a/p).
    """
    ls = pow(a, (p - 1) // 2, p)
    return ls if ls != p - 1 else -1

def quadratic_residues_or_non(p):
    """
    Находит множество квадратичных вычетов по модулю p.
    """
    residues = []
    non_residues = []
    for a in range(1, p):
        if legendre_symbol(a, p) == 1:
            residues.append(a)
        else:
            non_residues.append(a)
    return residues, non_residues


p = 7
residues, non_residues = quadratic_residues_or_non(p)
print("Множество квадратичных вычетов по модулю", p, ":", residues)
print("Множество квадратичных невычетов по модулю", p, ":", non_residues)