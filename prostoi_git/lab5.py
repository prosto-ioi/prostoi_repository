import re

def task1():
    text = input("Введите строку: ")
    x = re.findall(r"ab*", text)
    print(x)

def task2():
    text = input("Введите строку: ")
    x = re.findall(r"ab{2,3}", word)
    print(x)

def task3():
    text = input("Введите строку: ")
    x = re.findall(r"[a-z]+_[a-z]+", text)
    print(x) 

def task4():
    text = input("Введите строку: ")
    x = re.findall(r"[A-Z][a-z]+", text)
    print(x)    

def task5():
    text = input("Введите строку: ")
    x = re.findall(r"a.*b$", text)
    print(x)

def task6():
    text = input("Введите строку: ")
    x = re.sub("[, .]",":", text)
    print(x)

def task7():
    x = input("Введите snake_case строку: ")
    x = re.sub(r"_([a-z])", lambda x: x.group(1).upper(), s)
    print("Camel case:", x)

def task8():
    text = input("Введите строку: ")
    x = re.split("/1[A-Z]", text)
    print(x)

# def task9():
#     text = input("Введите строку (например, 'HelloWorldExample'): ")
#     re.sub(r"([A-Z])", r" \1", s)

# def task10():
#     text = input("Введите camelCase строку: ")
#     snake = re.sub(r'([A-Z])', r'_\1', text).lower()
#     print("✅ snake_case:", snake)


def main():
    tasks = {
        "1": ("Найти 'a' с нулем или более 'b'", task1),
        "2": ("Найти 'a' с 2–3 'b'", task2),
        "3": ("Найти строчные слова, соединённые '_'", task3),
        "4": ("Найти заглавную букву + строчные", task4),
        "5": ("Найти строку, где 'a' и заканчивается на 'b'", task5),
        "6": ("Заменить пробелы, запятые, точки на ':'", task6),
        "7": ("Преобразовать snake_case → camelCase", task7),
        "8": ("Разделить строку по заглавным буквам", task8),
        "9": ("Вставить пробелы между словами с заглавной буквы", task9),
        "10": ("Преобразовать camelCase → snake_case", task10),
    }

    while True:
        print("\n=== 🧩 Python RegEx Lab ===")
        for k, v in tasks.items():
            print(f"{k}. {v[0]}")
        print("0. Выход")

        choice = input("\nВыберите задание (0-10): ").strip()
        if choice == "0":
            print("👋 Выход из программы.")
            break
        elif choice in tasks:
            print(f"\n▶ Выполняется: {tasks[choice][0]}\n")
            tasks[choice][1]()
        else:
            print("⚠️ Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
