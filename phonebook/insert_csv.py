import csv
from connect import get_connection

def insert_from_csv(filename='sample.csv'):
    conn = get_connection()
    cur = conn.cursor()

    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute("""
                INSERT INTO phonebook(first_name, phone)
                VALUES (%s, %s)
                ON CONFLICT (phone) DO NOTHING;
            """, (row['first_name'], row['phone']))

    conn.commit()
    cur.close()
    conn.close()
    print("CSV uploaded!")

if __name__ == '__main__':
    insert_from_csv()
