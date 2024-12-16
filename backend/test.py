import psycopg2


def test_database_connection():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5433",
        )
        print("Коннект")
        conn.close()
    except psycopg2.Error as e:
        print(f"Не коннект: {e}")


if __name__ == "__main__":
    test_database_connection()
