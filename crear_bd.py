import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")

with psycopg.connect(database_url) as conn:
    with conn.cursor() as cur:

        cur.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL UNIQUE
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id SERIAL PRIMARY KEY,
            title VARCHAR(200) NOT NULL,
            content TEXT NOT NULL,
            category_id INT,
            FOREIGN KEY (category_id)
                REFERENCES categories(id)
                ON DELETE SET NULL
        );
        """)

        cur.execute("""
        INSERT INTO categories (id, name) VALUES
        (1, 'Tecnología'),
        (2, 'Negocios'),
        (3, 'Entretenimiento'),
        (4, 'Finanzas'),
        (5, 'Salud')
        ON CONFLICT (id) DO NOTHING;
        """)

        cur.execute("""
        INSERT INTO posts (id, title, content, category_id)
        VALUES (
            1,
            ' Bitcoin alcanza su máximo histórico en 2023',
            'El Bitcoin ha superado nuevamente las expectativas al alcanzar un nuevo máximo histórico de $45,000 este mes, impulsado por la adopción masiva de criptomonedas en países emergentes y el interés de grandes instituciones financieras. Analistas sugieren que este repunte se debe a la creciente demanda de activos digitales como alternativa a las monedas tradicionales. Sin embargo, expertos advierten sobre la volatilidad del mercado y recomiendan invertir con precaución. Mientras tanto, otras criptomonedas como Ethereum y Solana también han experimentado alzas significativas.',
            2
        )
        ON CONFLICT (id) DO NOTHING;
        """)

    conn.commit()

print("Base de datos creada correctamente.")