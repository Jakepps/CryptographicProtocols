class GaloisFieldCalculator:
    def __init__(self, modulus_poly, coeffs):
        self.modulus_poly = modulus_poly
        self.coeffs = coeffs
    
    def __add__(self, other):
        #                 коэффициенты многочленов                             для определения максимальной степепени результирующего полинома
        result_coeffs = [(self.coeffs[i] + other.coeffs[i]) % 2 for i in range(max(len(self.coeffs), len(other.coeffs)))]
        return GaloisFieldCalculator(self.modulus_poly, result_coeffs)

    def __mul__(self, other):
        result_coeffs = [0] * (len(self.coeffs) + len(other.coeffs) - 1)
        #вычисляем все возможные слагаемые в результирующем многочлене
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                result_coeffs[i+j] += self.coeffs[i] * other.coeffs[j]
        for i in range(len(result_coeffs)):
            result_coeffs[i] %= 2 #нужно чтобы коэфф.оставались в поле GF(2)
        return GaloisFieldCalculator(self.modulus_poly, result_coeffs)

    def __sub__(self, other):
        result_coeffs = [(self.coeffs[i] - other.coeffs[i]) % 2 for i in range(max(len(self.coeffs), len(other.coeffs)))]
        return GaloisFieldCalculator(self.modulus_poly, result_coeffs)

    def __truediv__(self, other):
        q = GaloisFieldCalculator(self.modulus_poly, [0]) #частное
        r = self #остаток
        while len(r.coeffs) >= len(other.coeffs): #пока степень остатка не будет >= степени делителя
            #определяем степени многочленов
            leading_degree = len(r.coeffs) - 1
            other_degree = len(other.coeffs) - 1
            #выравниваем степени текущего остатка с делителем перед выполнением деления
            q += GaloisFieldCalculator(self.modulus_poly, [0]*(leading_degree - other_degree) + [1])
            r -= (GaloisFieldCalculator(self.modulus_poly, [0]*(leading_degree - other_degree) + [1]) * other)
        return q, r

    def gcd(self, other):
        a, b = self, other
        while b != GaloisFieldCalculator(self.modulus_poly, [0]):
            a, b = b, a % b
        return a

    def __pow__(self, power):
        result = GaloisFieldCalculator(self.modulus_poly, [1])
        for _ in range(power):
            result *= self
        return result

    def multiplication_table(self):
        for i in range(1, len(self.coeffs)):
            for j in range(1, len(self.coeffs)):
                #                                                 создает список из i+j-1 нулей, а [1] добавляет единицу в конец списка, что соответствует элементу поля с нужной степенью
                result = GaloisFieldCalculator(self.modulus_poly, [0]*(i+j-1)+[1]) * GaloisFieldCalculator(self.modulus_poly, [0]*(i+j-1)+[1])
                print(f"{i} * {j} = {result.coeffs}")

def input_GaloisFieldCalculator(modulus_poly):
    coeffs = list(map(int, input("Введите коэффициенты многочлена через пробел: ").split()))
    return GaloisFieldCalculator(modulus_poly, coeffs)

def is_irreducible(poly):
    # перебираем все возможные делители степени многочлена poly, начиная с 1 и заканчивая половиной длины многочлена
    for i in range(1, len(poly) // 2 + 1):
        if len(poly) % i == 0:
            # разделяем многочлен на части равной длины i
            factors = [poly[j:j+i] for j in range(0, len(poly), i)]
            # проверяем, что все части, на которые был разделен многочлен, равны между собой
            if all(factor == factors[0] for factor in factors):
                return False
    return True

def input_modulus_poly():
    while True:
        coeffs = list(map(int, input("Введите коэффициенты образующего многочлена через пробел: ").split()))
        if is_irreducible(coeffs):
            return coeffs
        else:
            print("Многочлен не является неприводимым. Пожалуйста, введите неприводимый многочлен.")


def main():
    field_degree = int(input("Введите степень поля Галуа (степень двойки): "))
    modulus_poly_coeffs = input_modulus_poly() * field_degree
    modulus_poly = GaloisFieldCalculator(None, modulus_poly_coeffs)

    while True:
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. НОД")
        print("6. Возведение в степень")
        print("7. Таблица умножения")
        print("8. Выход")
        choice = int(input("Введите номер операции: "))

        if choice == 1:
            poly1 = input_GaloisFieldCalculator(modulus_poly)
            poly2 = input_GaloisFieldCalculator(modulus_poly)
            result = poly1 + poly2
            print("Результат:", result.coeffs)
        elif choice == 2:
            poly1 = input_GaloisFieldCalculator(modulus_poly)
            poly2 = input_GaloisFieldCalculator(modulus_poly)
            result = poly1 - poly2
            print("Результат:", result.coeffs)
        elif choice == 3:
            poly1 = input_GaloisFieldCalculator(modulus_poly)
            poly2 = input_GaloisFieldCalculator(modulus_poly)
            result = poly1 * poly2
            print("Результат:", result.coeffs)
        elif choice == 4:
            poly1 = input_GaloisFieldCalculator(modulus_poly)
            poly2 = input_GaloisFieldCalculator(modulus_poly)
            quotient, remainder = poly1 / poly2
            print("Частное:", quotient.coeffs)
            print("Остаток:", remainder.coeffs)
        elif choice == 5:
            poly1 = input_GaloisFieldCalculator(modulus_poly)
            poly2 = input_GaloisFieldCalculator(modulus_poly)
            gcd = poly1.gcd(poly2)
            print("НОД:", gcd.coeffs)
        elif choice == 6:
            poly = input_GaloisFieldCalculator(modulus_poly)
            power = int(input("Введите степень: "))
            result = poly ** power
            print("Результат:", result.coeffs)
        elif choice == 7:
            poly = input_GaloisFieldCalculator(modulus_poly)
            poly.multiplication_table()
        elif choice == 8:
            print("Выход...")
            break
        else:
            print("Неверный выбор операции.")
            continue

if __name__ == "__main__":
    main()