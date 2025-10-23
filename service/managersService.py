from models.managers import Manager
from extensions import db

# Funcion para el listado general
def listar_todos():
    return Manager.query.all()

# Funcion para buscar por ID
def buscar_por_id(id_manager):
    return Manager.query.get(id_manager)

# Funcion para buscar por estado
def buscar_por_estado(estado):
    return Manager.query.filter_by(estado=estado.upper()).all()

# Funcion para agregar manager
def agregar_manager(data):
    nuevo_manager = Manager(
        email=data['email'],
        username=data['username'],
        password=data['password']  
    )
    db.session.add(nuevo_manager)
    db.session.commit()
    return nuevo_manager

# Funcion para actualizar un manager
def actualizar_manager(id_manager, data):
    manager = Manager.query.get(id_manager)
    if not manager:
        return None

    manager.email = data.get('email', manager.email)
    manager.username = data.get('username', manager.username)
    manager.password = data.get('password', manager.password)
    manager.estado = data.get('estado', manager.estado)

    db.session.commit()
    return manager

# Eliminar lógico (estado = 'I')
def eliminar_manager(id_manager):
    manager = Manager.query.get(id_manager)
    if not manager:
        return None

    manager.estado = 'I'
    db.session.commit()
    return manager

#  Restaurar (estado = 'A')
def restaurar_manager(id_manager):
    manager = Manager.query.get(id_manager)
    if not manager:
        return None

    manager.estado = 'A'
    db.session.commit()
    return manager
