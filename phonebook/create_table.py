from connect import get_connection

def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            phone VARCHAR(20) UNIQUE NOT NULL
        )
        """,
    )

    conn = get_connection()
    cur = conn.cursor()
    for command in commands:
        cur.execute(command)

    conn.commit()
    cur.close()
    conn.close()
    print("Table created!")

if __name__ == '__main__':
    create_tables()
