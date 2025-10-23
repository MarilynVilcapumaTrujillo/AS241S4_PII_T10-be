from connection import get_connection

def test_connection():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT sysdate FROM dual")
        result = cursor.fetchone()
        print(f"🎉 Conexión exitosa. Fecha/hora actual en Oracle: {result[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print("❌ Error durante la prueba:", e)

if __name__ == "__main__":
    test_connection()
