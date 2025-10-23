import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

class Config:
    DB_USER = os.getenv("DB_USER", "MARILYN")
    DB_PASS = os.getenv("DB_PASS", "ProyectoJuana_2025")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "1521")
    DB_SERVICE = os.getenv("DB_SERVICE", "XEPDB1")

    # Cadena de conexión SQLAlchemy con python-oracledb (modo thin)
    SQLALCHEMY_DATABASE_URI = (
        f"oracle+oracledb://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/?service_name={DB_SERVICE}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
