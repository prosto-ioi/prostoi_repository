def generate_squares(n):
    """Генератор: квадраты чисел от 1 до n включительно."""
    for i in range(1, int(n) + 1):
        yield i * i

def even_numbers(n):
    """Генератор: чётные числа от 0 до n включительно."""
    n = int(n)
    for i in range(0, n + 1, 2):
        yield i

def divisible_by_3_and_4(n):
    """Генератор: числа между 0 и n, делящиеся и на 3 и на 4.
    (LCM(3,4) = 12 — поэтому шаг 12)."""
    n = int(n)
    for i in range(0, n + 1, 12):
        yield i

def squares(a, b):
    """Генератор: квадраты чисел от a до b включительно.
    Если a > b — автоматически поменяем местами."""
    a = int(a); b = int(b)
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        yield i * i

def main():
    while True:
        print("\nВыберите действие:")
        print("1 — Генератор квадратов до N (1..N)")
        print("2 — Чётные числа от 0 до N (через запятую)")
        print("3 — Числа, делящиеся на 3 и 4, от 0 до N")
        print("4 — Генератор squares(a, b)")
        print("0 — Выход")
        choice = input("Ваш выбор: ").strip()

        if choice == "0":
            print("Выход из программы.")
            break
        elif choice == "1":
            n = int(input("Введите N: "))
            print("Квадраты:", list(generate_squares(n)))
        elif choice == "2":
            n = int(input("Введите N: "))
            print("Чётные через запятую:", ",".join(str(x) for x in even_numbers(n)))
        elif choice == "3":
            n = int(input("Введите N: "))
            print("Делятся на 3 и 4:", list(divisible_by_3_and_4(n)))
        elif choice == "4":
            a = int(input("a = "))
            b = int(input("b = "))
            print("Квадраты от {} до {}:".format(a, b))
            for x in squares(a, b):
                print(x)
        else:
            print("Неверный выбор, попробуйте ещё раз.")

if __name__ == "__main__":
    main()
