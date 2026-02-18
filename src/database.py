import psycopg2

def get_db_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="ecommerce_db",
            user="ecommerce_user",
            password="wordpass"
        )
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

    return connection