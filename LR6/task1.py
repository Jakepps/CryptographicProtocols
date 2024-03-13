import random

# task 1
# Параметры эллиптической кривой и модуля
a = -1
b = 1
p = 751
G = (0, 1)

# Модульная инверсия 
def modinv(a, p):
    return pow(a, p - 2, p)

# Сложение двух точек P и Q на эллиптической кривой
def point_add(P, Q):
    if P == (0, 0): 
        return Q
    if Q == (0, 0): 
        return P
    if P == Q: 
        return point_double(P)
    xp, yp = P
    xq, yq = Q
    if xp == xq and yp == p - yq: 
        return (0, 0)
    lam = (yq - yp) * modinv(xq - xp, p) % p
    x = (lam ** 2 - xp - xq) % p
    y = (lam * (xp - x) - yp) % p
    return (x, y)

# Удвоение точки P на кривой
def point_double(P):
    if P == (0, 0): 
        return P
    xp, yp = P
    lam = (3 * xp ** 2 + a) * modinv(2 * yp, p) % p
    x = (lam ** 2 - 2 * xp) % p
    y = (lam * (xp - x) - yp) % p
    return (x, y)

# Умножение точки P на скаляр n
def point_multiply(P, n):
    R = (0, 0)
    N = P
    while n:
        if n & 1: 
            R = point_add(R, N)
        N = point_double(N)
        n >>= 1
    return R

# Генерация ключей
def generate_keys():
    nb = random.randint(1, p - 1)
    Pb = point_multiply(G, nb)
    return nb, Pb

# Шифрование
def encrypt(Pm, k, Pb):
    C1 = point_multiply(G, k)
    C2 = point_add(Pm, point_multiply(Pb, k))
    return C1, C2

# Функция для инвертирования точки
def point_negate(P):
    x, y = P
    return (x, p - y) if y != 0 else P

# Дешифрование
def decrypt(C1, C2, nb):
    return point_add(C2, point_negate(point_multiply(C1, nb)))

def decrypt_to_text(decrypted_points, alphabet):
    # Инвертирование алфавита для поиска символов по точкам
    points_to_char = {point: char for char, point in alphabet.items()}
    # Сопоставление каждой точки с символом
    return ''.join(points_to_char.get(point, '?') for point in decrypted_points)

alphabet = {'л': (240, 399), 'а': (93, 484), 'т': (247, 266),
            'ы': (247, 485), 'ш': (236, 399), 'с': (243, 664), 'к': (105, 382), 'и': (102, 484),
            'й': (236, 712), 'е': (234, 587),'р': (243, 87),'п': (240, 442),'в': (229, 151),
            'о': (240, 309)}

message = 'терпеливо'

nb, Pb = generate_keys()
k_values = [random.randint(1, p - 1) for _ in range(len(message))]
ciphertext = [encrypt(alphabet[char], k, Pb) for char, k in zip(message, k_values)]
decrypted_points = [decrypt(C1, C2, nb) for C1, C2 in ciphertext]
decrypted_message = decrypt_to_text(decrypted_points, alphabet)

print("Исходное сообщение:", message)
print("Исходный алфавит:", alphabet)
print("Секретный ключ (nb):", nb)
print("Открытый ключ (Pb):", Pb)
print("Шифротекст:", ciphertext)
print("Полученный точки:", decrypted_points)
print("Полученный текст:", decrypted_message)
print("\n")
