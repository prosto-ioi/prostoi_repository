import psycopg2
from connect import get_connection


def init_database():
    sql_code = """

    CREATE OR REPLACE PROCEDURE upsert_user(p_name TEXT, p_phone TEXT)
    LANGUAGE plpgsql AS $$
    BEGIN
        IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_name) THEN
            UPDATE phonebook
            SET phone = p_phone
            WHERE first_name = p_name;
        ELSE
            INSERT INTO phonebook(first_name, phone)
            VALUES (p_name, p_phone);
        END IF;
    END;
    $$;

    CREATE OR REPLACE FUNCTION search_pattern(p_pattern TEXT)
    RETURNS TABLE(
        id INT,
        first_name VARCHAR,
        phone VARCHAR
    )
    LANGUAGE plpgsql AS $$
    BEGIN
        RETURN QUERY
        SELECT pb.id, pb.first_name, pb.phone
        FROM phonebook pb
        WHERE pb.first_name ILIKE '%' || p_pattern || '%'
           OR pb.phone ILIKE '%' || p_pattern || '%';
    END;
    $$;

    CREATE OR REPLACE FUNCTION get_page(p_limit INT, p_offset INT)
    RETURNS TABLE(
        id INT,
        first_name VARCHAR,
        phone VARCHAR
    )
    LANGUAGE plpgsql AS $$
    BEGIN
        RETURN QUERY
        SELECT pb.id, pb.first_name, pb.phone
        FROM phonebook pb
        ORDER BY pb.id
        LIMIT p_limit OFFSET p_offset;
    END;
    $$;

    CREATE OR REPLACE PROCEDURE delete_user(p_name TEXT, p_phone TEXT)
    LANGUAGE plpgsql AS $$
    BEGIN
        DELETE FROM phonebook
        WHERE first_name = p_name
           OR phone = p_phone;
    END;
    $$;

    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql_code)
            conn.commit()
        print("Database initialized successfully!")

    except Exception as error:
        print("Error while initializing DB:")
        print(error)


if __name__ == "__main__":
    init_database()
