from models.empleado import Empleado
from extensions import db

def listarEmpleados():
    return Empleado.query.all()

def buscarPorId(id_empleado):
    return Empleado.query.get(id_empleado)

def buscarPorEstado(estado):
    return Empleado.query.filter_by(estado=estado.upper()).all()

def agregarEmpleado(data):
    nuevo_empleado = Empleado(
        tipo_documento=data.get("tipo_documento"),
        num_documento=data.get("num_documento"),
        nombres=data.get("nombres"),
        apellidos=data.get("apellidos"),
        cargo=data.get("cargo"),
        area=data.get("area"),
    )
    db.session.add(nuevo_empleado)
    db.session.commit()
    return nuevo_empleado

def actualizarEmpleado(id_empleado, data):
        empleado = Empleado.query.get(id_empleado)
        if not empleado:
           return None
        
        empleado.tipo_documento = data.get("tipo_documento", empleado.tipo_documento)
        empleado.num_documento = data.get("num_documento", empleado.num_documento)
        empleado.nombres = data.get("nombres", empleado.nombres)
        empleado.apellidos = data.get("apellidos", empleado.apellidos)
        empleado.cargo = data.get("cargo", empleado.cargo)
        empleado.area = data.get("area", empleado.area)

        db.session.commit()
        return empleado

def eliminarLogicamenteEmpleado(id_empleado):
    empleado = Empleado.query.get(id_empleado)
    if not empleado:
        return None

    empleado.estado = 'I'
    db.session.commit()
    return empleado

def restaurarEmpleado(id_empleado):
    empleado = Empleado.query.get(id_empleado)
    if not empleado:
        return None

    empleado.estado = 'A'
    db.session.commit()
    return empleado
