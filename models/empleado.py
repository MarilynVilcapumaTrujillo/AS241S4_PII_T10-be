from extensions import db
from datetime import datetime
from collections import OrderedDict

class Empleado(db.Model):
    __tablename__ = 'empleado'

    id_empleado = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Columna autoincrementable
    tipo_documento = db.Column(db.CHAR(3), nullable=False)
    num_documento = db.Column(db.String(20), nullable=False, unique=True)
    nombres = db.Column(db.String(60), nullable=False)
    apellidos = db.Column(db.String(60), nullable=False)
    cargo = db.Column(db.String(30), nullable=False)
    area = db.Column(db.String(50), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  # Fecha de registro
    estado = db.Column(db.CHAR(1), default='A', nullable=False)  # A=Activo, I=Inactivo

    def as_dict(self):
        return {
            "id_empleado": self.id_empleado,
            "tipo_documento": self.tipo_documento,
            "num_documento": self.num_documento,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "cargo": self.cargo,
            "area": self.area,
            "estado": self.estado,
            "fecha_registro": self.fecha_registro.strftime("%Y-%m-%d %H:%M:%S") if self.fecha_registro else None
        }