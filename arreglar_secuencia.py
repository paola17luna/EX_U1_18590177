import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")

with psycopg.connect(database_url) as conn:
    with conn.cursor() as cur:

        cur.execute("""
        SELECT setval(
            pg_get_serial_sequence('posts', 'id'),
            COALESCE((SELECT MAX(id) FROM posts), 1),
            true
        );
        """)

        cur.execute("""
        SELECT setval(
            pg_get_serial_sequence('categories', 'id'),
            COALESCE((SELECT MAX(id) FROM categories), 1),
            true
        );
        """)

    conn.commit()

print("Secuencias corregidas correctamente.")