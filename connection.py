import oracledb
from config import Config

def get_connection():
    try:
        # Inicializar el cliente Oracle con wallet
        oracledb.init_oracle_client(config_dir=Config.wallet_path)
        print(" Cliente Oracle inicializado")

        connection = oracledb.connect(
            user=Config.user,
            password=Config.password,
            dsn=Config.dsn,
            config_dir=Config.wallet_path,
            wallet_location=Config.wallet_path,
            wallet_password=Config.wallet_password
        )

        print(" Conexión establecida correctamente con Oracle Autonomous DB (Wallet interna)")
        return connection

    except Exception as e:
        print("Error al conectar:", e)
        raise
