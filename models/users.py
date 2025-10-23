from extensions import db
from datetime import datetime

class Users(db.Model):
    __tablename__ = 'users'

    users_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)
    user_type = db.Column(db.String(100), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    state = db.Column(db.String(1), default='A', nullable=False)

    def as_dict(self):
        """Convierte el objeto en un diccionario (útil para jsonify)."""
        return {
            "users_id": self.users_id,
            "employee_id": self.employee_id,
            "username": self.username,
            "password": self.password,  # puedes omitirlo si no quieres exponerlo
            "user_type": self.user_type,
            "creation_date": self.creation_date.strftime("%Y-%m-%d %H:%M:%S") if self.creation_date else None,
            "state": self.state
        }
