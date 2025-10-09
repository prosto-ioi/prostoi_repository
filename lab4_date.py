from datetime import date, datetime, timedelta

def subtract_five_days():
    today = date.today()
    result = today - timedelta(days=5)
    print(f"Сегодня: {today}")
    print(f"Дата 5 дней назад: {result}")

def print_yesterday_today_tomorrow():
    today = date.today()
    print(f"Вчера: {today - timedelta(days=1)}")
    print(f"Сегодня: {today}")
    print(f"Завтра: {today + timedelta(days=1)}")

def drop_microseconds():
    now = datetime.now()
    print("Текущее время:", now)
    print("Без микросекунд:", now.replace(microsecond=0))

def date_difference_seconds():
    print("Введите первую дату (в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС):")
    d1_str = input("Дата 1: ")
    print("Введите вторую дату:")
    d2_str = input("Дата 2: ")
    try:
        d1 = datetime.strptime(d1_str, "%Y-%m-%d %H:%M:%S")
        d2 = datetime.strptime(d2_str, "%Y-%m-%d %H:%M:%S")
        diff = abs((d2 - d1).total_seconds())
        print(f"Разница между датами: {diff} секунд")
    except ValueError:
        print("Ошибка: формат даты должен быть ГГГГ-ММ-ДД ЧЧ:ММ:СС")

def main():
    while True:
        print("1 — Вычесть 5 дней из текущей даты")
        print("2 — Показать вчера, сегодня, завтра")
        print("3 — Убрать микросекунды из текущего времени")
        print("4 — Разница между двумя датами (в секундах)")
        print("0 — Выход")

        choice = input("Ваш выбор: ").strip()
        if choice == "1":
            subtract_five_days()
        elif choice == "2":
            print_yesterday_today_tomorrow()
        elif choice == "3":
            drop_microseconds()
        elif choice == "4":
            date_difference_seconds()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор, попробуйте ещё раз.")

if __name__ == "__main__":
    main()
