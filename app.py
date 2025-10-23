from flask import Flask
from config import Config
from extensions import db
from routes.managersRoutes import manager_bp
from routes.empleadoRoutes import empleado_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)

    

    # Registrar rutas
    app.register_blueprint(manager_bp)
    app.register_blueprint(empleado_bp)


    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
