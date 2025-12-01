from connect import get_connection
from insert_csv import insert_from_csv

def insert_user():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO phonebook(first_name, phone)
        VALUES (%s, %s)
        ON CONFLICT (phone) DO NOTHING;
    """, (name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print("User inserted!")


def update_user():
    phone = input("Enter phone of user to update: ")

    print("1) Change name")
    print("2) Change phone")
    choice = input("Choose: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        new_name = input("Enter new name: ")
        cur.execute("UPDATE phonebook SET first_name=%s WHERE phone=%s",
                    (new_name, phone))

    elif choice == "2":
        new_phone = input("Enter new phone: ")
        cur.execute("UPDATE phonebook SET phone=%s WHERE phone=%s",
                    (new_phone, phone))

    conn.commit()
    cur.close()
    conn.close()
    print("Updated!")


def search_users():
    print("1) Find by name")
    print("2) Find by phone")
    choice = input("Choose: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        name = input("Name: ")
        cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s",
                    ('%' + name + '%',))
    else:
        phone = input("Phone: ")
        cur.execute("SELECT * FROM phonebook WHERE phone=%s", (phone,))

    rows = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    conn.close()


def delete_user():
    phone = input("Phone to delete: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))

    conn.commit()
    cur.close()
    conn.close()
    print("Deleted!")


def menu():
    while True:
        print("\n MENU ")
        print("1) Insert user manually")
        print("2) Upload csv")
        print("3) Update user")
        print("4) Search user")
        print("5) Delete user")
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
            delete_user()
        elif choice == "0":
            break
        else:
            print("Wrong input!")

if __name__ == '__main__':
    menu()
