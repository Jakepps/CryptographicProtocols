def find_cyclotomic_classes(n):
    modulus = 2 ** n - 1
    classes = []
    found = set()
    for i in range(1, modulus + 1):  # Учитываем все элементы до 2^n - 1
        if i not in found:
            current_class = set()
            value = i
            while value not in current_class:
                current_class.add(value)
                found.add(value)
                value = (value * 2) % (modulus + 1)
            classes.append(sorted(current_class)[1:])
    print(f"Цикломатические классы для GF(2^{n}):")
    return classes


def binary_to_polynomial(binary):
    binary_str = bin(binary)[2:]
    result = ""
    degree = len(binary_str) - 1
    for i, bit in enumerate(binary_str):
        if bit == '1':
            if degree - i > 1:
                result += f"x^{degree - i} + "
            elif degree - i == 1:
                result += "x + "
            else:
                result += "1"
    if result.endswith(" + "):
        result = result[:-3]
    return result


def multiply_by_alpha(alpha, modulus, n):
    # Умножение alpha на x с учетом степени n для GF(2^n)
    result = alpha << 1
    # Проверяем, превышает ли результат предел для GF(2^n)
    if result >= 2 ** n:
        result ^= modulus  # Редукция по модулю образующего многочлена (XOR)
    return result

def reduce_alpha(alpha, modulus, m):
    max_degree = 2**(m)  # Максимально возможное значение для GF(2^m) равно 2^m, а не 2^(m-1)
    while alpha >= max_degree:
        # Находим степень текущего alpha
        degree_alpha = alpha.bit_length() - 1
        # Находим степень модуля
        degree_modulus = modulus.bit_length() - 1
        # Проверяем, что degree_alpha >= degree_modulus для корректного сдвига
        if degree_alpha >= degree_modulus:
            # Сдвигаем модуль на разницу степеней
            shifted_modulus = modulus << (degree_alpha - degree_modulus)
            # Применяем XOR для редукции
            alpha ^= shifted_modulus
        else:
            # Если alpha меньше степени модуля, дальнейшая редукция не требуется
            break
    return alpha

def generate_elements_and_minimal_polynomials(n, modulus, alpha=0b10):
    # Начинаем с 1 (единичный многочлен)
    elements = [1]
    alpha = reduce_alpha(alpha, modulus, n)
    # Начальное значение alpha по умолчанию: (x)
    for _ in range(1, 2 ** n - 1):  # Генерируем все элементы поля GF(2^n)
        alpha = multiply_by_alpha(alpha, modulus, n)
        elements.append(alpha)

    # Выводим элементы поля и их полиномиальное представление
    print("Элементы поля GF(2^{}):".format(n))
    for element in elements:
        print(binary_to_polynomial(element))
    
#task 1-2
print("Задание 1, для полинома 11001")
generate_elements_and_minimal_polynomials(4,0b11001)

print("\nЗадание 2, для полинома 10011")
generate_elements_and_minimal_polynomials(4,0b10011)

#task 3-6
print("\nЗадание 3-6")
print(find_cyclotomic_classes(5))
print("Циклотомический класс и минимальный многочлен для x:")
generate_elements_and_minimal_polynomials(5,0b100101,0b10)
print("\nЦиклотомический класс и минимальный многочлен для x^3:")
generate_elements_and_minimal_polynomials(5,0b100101,0b100)
print("\nЦиклотомический класс и минимальный многочлен для x^5:")
generate_elements_and_minimal_polynomials(5,0b100101,0b10000)
print("\nЦиклотомический класс и минимальный многочлен для x^7:")
generate_elements_and_minimal_polynomials(5,0b100101,0b1000000)

#task 7