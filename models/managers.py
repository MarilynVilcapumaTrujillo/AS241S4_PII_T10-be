from extensions import db
from datetime import datetime
from collections import OrderedDict


class Manager(db.Model):
    __tablename__ = 'manager'

    id_manager = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.String(1), default='A') 

    def as_dict(self):
        return {
            "id_manager": self.id_manager,
            "email": self.email,
            "username": self.username,
            "password": self.password,  
            "estado": self.estado,
            "fecha_registro": self.fecha_registro.strftime("%Y-%m-%d %H:%M:%S") if self.fecha_registro else None
        }


    