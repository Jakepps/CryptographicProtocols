class GaloisFieldCalculator:
    def __init__(self, modulus_poly, degree):
        self.modulus_poly = modulus_poly
        self.degree = degree

    def add(self, a, b):
        return (a + b) % 2

    def subtract(self, a, b):
        return (a - b) % 2

    def multiply(self, a, b):
        result = 0
        while b:
            if b & 1: #проверяем является ли младший бит b равный 1
                result ^= a #XOR выполняется для умножения чисел в поле Галуа
            a <<= 1 # сдвигается на один бит влево с помощью операции a <<= 1, это эквивалентно умножению a на 2
            if a & (1 << self.degree): #проверяем не превышает ли степени поля
                a ^= self.modulus_poly #нужно для выполнения операции модуляции,тк мы работаем в поле Галуа и должны оставаться в пределах его элементов
            b >>= 1
        return result

    def divide(self, a, b):
        quotient = 0
        while a >= b:
            shift = len(bin(a)) - len(bin(b)) # на сколько бит нужно сдвинуть b, чтобы его старший бит совпал со старшим битом a
            a ^= b << shift
            quotient |= 1 << shift
        return quotient

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def power(self, base, exponent):
        result = 1
        while exponent:
            if exponent & 1:
                result = self.multiply(result, base)
            base = self.multiply(base, base)
            exponent >>= 1
        return result

    def multiplication_table(self):
        table = [[0] * 2**self.degree for _ in range(2**self.degree)]
        for i in range(2**self.degree):
            for j in range(2**self.degree):
                table[i][j] = self.multiply(i, j)
        return table

def parse_polynomial(polynomial_str):
    return int(polynomial_str.replace(" ", ""), 2)

def main():
    degree = int(input("Введите степень поля Галуа: "))
    modulus_poly_str = input("Введите образующий многочлен в двоичной форме через пробел: ")
    modulus_poly = parse_polynomial(modulus_poly_str)
    gf_calculator = GaloisFieldCalculator(modulus_poly, degree)
    
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

        if choice == 8:
            print("Выход...")
            break

        if choice == 1:
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
            result = gf_calculator.add(a, b)
            print("Результат сложения:", result)
        elif choice == 2:
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
            result = gf_calculator.subtract(a, b)
            print("Результат вычитания:", result)
        elif choice == 3:
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
            result = gf_calculator.multiply(a, b)
            print("Результат умножения:", a, "*", b, "=", result)
        elif choice == 4:
            a = int(input("Введите делимое: "))
            b = int(input("Введите делитель: "))
            result = gf_calculator.divide(a, b)
            print("Результат деления:", a, "/", b, "=", result)
        elif choice == 5:
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
            result = gf_calculator.gcd(a, b)
            print("НОД чисел:", result)
        elif choice == 6:
            base = int(input("Введите основание: "))
            exponent = int(input("Введите показатель степени: "))
            result = gf_calculator.power(base, exponent)
            print("Результат возведения в степень:", base, "^", exponent, "=", result)
        elif choice == 7:
            print("Таблица умножения:")
            table = gf_calculator.multiplication_table()
            for i in range(2**degree):
                for j in range(2**degree):
                    print(f"{i}*{j}={table[i][j]}", end="\t")
                print()
            continue
        else:
            print("Неверный выбор операции.")

if __name__ == "__main__":
    main()