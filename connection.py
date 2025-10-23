import oracledb
from config import Config

def get_connection():
    try:
        # Usamos modo thin (no requiere cliente Oracle ni wallet)
        conn = oracledb.connect(
            user=Config.DB_USER,
            password=Config.DB_PASS,
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            service_name=Config.DB_SERVICE
        )
        return conn
    except Exception as e:
        print("❌ Error de conexión:", e)
        raise
