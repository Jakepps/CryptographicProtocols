def add(x, y, p):
    return (x + y) % p

def subtract(x, y, p):
    return (x - y) % p

def multiply(x, y, p):
    return (x * y) % p

def division(x, y, p):
    gcd_xy = gcd(x, y)
    if gcd_xy != 1:
        raise ValueError("Деление невозможно в конечном поле!")
    return (x * pow(y, p - 2, p)) % p

def power(x, n, p):
    return pow(x, n, p)

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def multiplication_table(p):
    print("Таблица умножения:")
    for i in range(p):
        for j in range(p):
            print(f"{i} * {j} = {multiply(i, j, p)}")
        print()

def main():
    try:
        p = int(input("Введите простое число (p) для конечного поля: "))
        polynomial = input("Введите коэффициенты многочлена, разделяя их пробелом: ").split()
        polynomial = [int(coeff) for coeff in polynomial]

        while True:
            print("\nВыберите операцию:")
            print("1. Сложение")
            print("2. Вычитание")
            print("3. Умножение")
            print("4. Деление")
            print("5. Степень")
            print("6. НОД")
            print("7. Таблица умножения")
            print("8. Выход")

            choice = int(input("Введите свой выбор: "))

            if choice == 8:
                print("Выход...")
                break

            if choice > 8 or choice < 1:
                print("Ввидите номер операции из представленных!")
                continue

            x = int(input("Ввидите первый операнд: "))
            y = int(input("Ввидите второй операнд: "))

            if choice == 1:
                result = add(x, y, p)
            elif choice == 2:
                result = subtract(x, y, p)
            elif choice == 3:
                result = multiply(x, y, p)
            elif choice == 4:
                result = division(x, y, p)
            elif choice == 5:
                result = power(x, y, p)
            elif choice == 6:
                result = gcd(x, y)
            elif choice == 7:
                multiplication_table(p)
                continue

            print("Результат:", result)

    except ValueError:
        print("Неверный ввод. Пожалуйста, введите действительный номер операции.")

if __name__ == "__main__":
    main()
