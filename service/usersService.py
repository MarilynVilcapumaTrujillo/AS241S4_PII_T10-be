from models.users import Users
from extensions import db

# Listar todos los usuarios
def listar_todos():
    return Users.query.all()

# Buscar usuario por ID
def buscar_por_id(users_id):
    return Users.query.get(users_id)

# Buscar usuarios por estado (A o I)
def buscar_por_estado(state):
    return Users.query.filter_by(state=state.upper()).all()

# Agregar nuevo usuario
def agregar_usuario(data):
    nuevo_usuario = Users(
        employee_id=data['employee_id'],
        username=data['username'],
        password=data['password'],
        user_type=data['user_type'],
        state=data.get('state', 'A')
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return nuevo_usuario

# Actualizar usuario existente
def actualizar_usuario(users_id, data):
    usuario = Users.query.get(users_id)
    if not usuario:
        return None

    usuario.employee_id = data.get('employee_id', usuario.employee_id)
    usuario.username = data.get('username', usuario.username)
    usuario.password = data.get('password', usuario.password)
    usuario.user_type = data.get('user_type', usuario.user_type)
    usuario.state = data.get('state', usuario.state)

    db.session.commit()
    return usuario

# Eliminar lógico (marcar como inactivo)
def eliminar_usuario(users_id):
    usuario = Users.query.get(users_id)
    if not usuario:
        return None

    usuario.state = 'I'
    db.session.commit()
    return usuario

# Restaurar usuario (volver a activo)
def restaurar_usuario(users_id):
    usuario = Users.query.get(users_id)
    if not usuario:
        return None

    usuario.state = 'A'
    db.session.commit()
    return usuario
