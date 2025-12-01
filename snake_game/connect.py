import psycopg2
from config import load_config

def get_connection():
    cfg = load_config()
    conn = psycopg2.connect(**cfg)
    conn.set_client_encoding('UTF8')
    return conn

