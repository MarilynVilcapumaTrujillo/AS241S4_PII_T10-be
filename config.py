import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASS")
    dsn = os.getenv("DB_TNS_NAME")

    # Wallet local
    wallet_path = "Wallet_SeguimientoVacaciones"
    wallet_password = "Gojo25092023$!"

    # SQLAlchemy URI
    SQLALCHEMY_DATABASE_URI = (
        f"oracle+oracledb://{user}:{password}@{dsn}"
        f"?config_dir={wallet_path}&wallet_location={wallet_path}"
        f"&wallet_password={wallet_password}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 3,
        'max_overflow': 5,
        'pool_timeout': 30,
        'pool_recycle': 1800,
        'pool_pre_ping': True,
        'echo': False,
        'echo_pool': False,
    }

    print(f"Usando wallet interna en: {wallet_path}")
    print(f"DSN configurado: {dsn}")
