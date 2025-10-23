from connection import get_connection

def test_connection():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 'Conexión exitosa a Oracle XE' FROM dual")
        result = cursor.fetchone()
        print("✅", result[0])
        cursor.close()
        conn.close()
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    test_connection()
