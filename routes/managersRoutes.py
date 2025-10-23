from flask import Blueprint, request, jsonify
import service.managersService as service

manager_bp = Blueprint('manager', __name__, url_prefix='/manager')

# Endpint para el listado general
@manager_bp.route('/', methods=['GET'])
def listar_todos():
    managers = service.listar_todos()
    return jsonify([m.as_dict() for m in managers]), 200

# Endpoint para buscar por ID
@manager_bp.route('/<int:id_manager>', methods=['GET'])
def buscar_por_id(id_manager):
    manager = service.buscar_por_id(id_manager)
    if not manager:
        return jsonify({"message": "Manager no encontrado"}), 404
    return jsonify(manager.as_dict()), 200

# Endpoint para buscar por estado
@manager_bp.route('/estado/<string:estado>', methods=['GET'])
def buscar_por_estado(estado):
    managers = service.buscar_por_estado(estado)
    return jsonify([m.as_dict() for m in managers]), 200

# Endpiint para agregar manager
@manager_bp.route('/save', methods=['POST'])
def agregar_manager():
    data = request.get_json()
    manager = service.agregar_manager(data)
    return jsonify(manager.as_dict()), 201

# Endpoint para actualizar un manager
@manager_bp.route('/update/<int:id_manager>', methods=['PUT'])
def actualizar_manager(id_manager):
    data = request.get_json()
    manager = service.actualizar_manager(id_manager, data)
    if not manager:
        return jsonify({"message": "Manager no encontrado"}), 404
    return jsonify(manager.as_dict()), 200

# Eliminar lógico
@manager_bp.route('/eliminar/<int:id_manager>', methods=['PATCH'])
def eliminar_manager(id_manager):
    manager = service.eliminar_manager(id_manager)
    if not manager:
        return jsonify({"message": "Manager no encontrado"}), 404
    return jsonify({"message": "Manager eliminado lógicamente"}), 200

# Restaurado logivo
@manager_bp.route('/restaurar/<int:id_manager>', methods=['PATCH'])
def restaurar_manager(id_manager):
    manager = service.restaurar_manager(id_manager)
    if not manager:
        return jsonify({"message": "Manager no encontrado"}), 404
    return jsonify({"message": "Manager restaurado correctamente"}), 200
