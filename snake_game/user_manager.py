from connect import get_connection

def get_or_create_user(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, current_level FROM users WHERE username=%s", (username,))
    user = cur.fetchone()
    if user:
        user_id, level = user
        print(f"Welcome back, {username}! Your current level: {level}")
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        level = 1
        print(f"New user {username} created. Starting at level {level}.")
    cur.close()
    conn.close()
    return user_id, level

def save_score(user_id, score, level):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)",
        (user_id, score, level)
    )
    cur.execute("UPDATE users SET current_level=%s WHERE id=%s", (level, user_id))
    conn.commit()
    cur.close()
    conn.close()
