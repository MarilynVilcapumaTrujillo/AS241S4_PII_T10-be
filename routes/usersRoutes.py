from flask import Blueprint, request, jsonify
import service.usersService as service


# Blueprint para usuarios
users_bp = Blueprint('users', __name__, url_prefix='/users')

# Listar todos los usuarios
@users_bp.route('/', methods=['GET'])
def listar_todos():
    usuarios = service.listar_todos()
    return jsonify([u.as_dict() for u in usuarios]), 200

# Buscar usuario por ID
@users_bp.route('/<int:users_id>', methods=['GET'])
def buscar_por_id(users_id):
    usuario = service.buscar_por_id(users_id)
    if not usuario:
        return jsonify({"message": "Usuario no encontrado"}), 404
    return jsonify(usuario.as_dict()), 200

# Buscar usuarios por estado (A o I)
@users_bp.route('/estado/<string:state>', methods=['GET'])
def buscar_por_estado(state):
    usuarios = service.buscar_por_estado(state)
    return jsonify([u.as_dict() for u in usuarios]), 200

# Agregar nuevo usuario
@users_bp.route('/save', methods=['POST'])
def agregar_usuario():
    data = request.get_json()
    usuario = service.agregar_usuario(data)
    return jsonify(usuario.as_dict()), 201

# Actualizar usuario existente
@users_bp.route('/update/<int:users_id>', methods=['PUT'])
def actualizar_usuario(users_id):
    data = request.get_json()
    usuario = service.actualizar_usuario(users_id, data)
    if not usuario:
        return jsonify({"message": "Usuario no encontrado"}), 404
    return jsonify(usuario.as_dict()), 200

# Eliminar lógico (marcar como inactivo)
@users_bp.route('/eliminar/<int:users_id>', methods=['PATCH'])
def eliminar_usuario(users_id):
    usuario = service.eliminar_usuario(users_id)
    if not usuario:
        return jsonify({"message": "Usuario no encontrado"}), 404
    return jsonify({"message": "Usuario eliminado lógicamente"}), 200

# Restaurar usuario (volver a activo)
@users_bp.route('/restaurar/<int:users_id>', methods=['PATCH'])
def restaurar_usuario(users_id):
    usuario = service.restaurar_usuario(users_id)
    if not usuario:
        return jsonify({"message": "Usuario no encontrado"}), 404
    return jsonify({"message": "Usuario restaurado correctamente"}), 200
