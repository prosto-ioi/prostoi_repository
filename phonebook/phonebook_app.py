from connect import get_connection
from insert_csv import insert_from_csv


def insert_user():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    sql = "CALL upsert_user(%s, %s);"

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, phone))
                conn.commit()
        print("User inserted/updated via procedure!")
    except Exception as error:
        print("Error:", error)


def update_user():
    name = input("Enter username to update: ")
    phone = input("Enter new phone: ")

    sql = "CALL upsert_user(%s, %s);"

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, phone))
                conn.commit()
        print("Updated via procedure!")
    except Exception as error:
        print("Error:", error)

def search_users():
    pattern = input("Enter part of name or phone: ")

    sql = "SELECT * FROM search_pattern(%s);"

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (pattern,))
                rows = cur.fetchall()

        for r in rows:
            print(r)

    except Exception as error:
        print("Error:", error)


def pagination():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))

    sql = "SELECT * FROM get_page(%s, %s);"

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (limit, offset))
                rows = cur.fetchall()

        for r in rows:
            print(r)

    except Exception as error:
        print("Error:", error)


def delete_user():
    print("1) Delete by name")
    print("2) Delete by phone")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = None
    else:
        name = None
        phone = input("Enter phone: ")

    sql = "CALL delete_user_proc(%s, %s);"

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, phone))
                conn.commit()
        print("Deleted via procedure!")
    except Exception as error:
        print("Error:", error)


def menu():
    while True:
        print("\n MENU ")
        print("1) Insert user")
        print("2) Upload CSV")
        print("3) Update user")
        print("4) Search users")
        print("5) Pagination")
        print("6) Delete user")
        print("0) Exit")

        choice = input("Choose option: ")

        if choice == "1":
            insert_user()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            update_user()
        elif choice == "4":
            search_users()
        elif choice == "5":
            pagination()
        elif choice == "6":
            delete_user()
        elif choice == "0":
            break
        else:
            print("Wrong input!")


if __name__ == '__main__':
    menu()
