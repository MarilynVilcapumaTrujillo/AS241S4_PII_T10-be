from flask import Blueprint, request, jsonify
import service.empleadoService as service

empleado_bp = Blueprint("empleado", __name__, url_prefix = '/empleado')

# Endpoint para el listado general
@empleado_bp.route('/', methods=['GET'])
def listarEmpleados():
    empleados = service.listarEmpleados()
    return jsonify([e.as_dict() for e in empleados]), 200

# Endpoint para buscar por ID
@empleado_bp.route('/<int:id_empleado>', methods=['GET'])
def buscarPorId(id_empleado):
    empleado = service.buscarPorId(id_empleado)
    if empleado:
        return jsonify(empleado.as_dict()), 200
    return jsonify({"error": "Empleado no encontrado"}), 404

# Endpoint para buscar por estado
@empleado_bp.route('/estado/<estado>', methods=['GET'])
def buscarPorEstado(estado):
    empleados = service.buscarPorEstado(estado)
    return jsonify([e.as_dict() for e in empleados]), 200

# Endpoint para agregar un nuevo empleado
@empleado_bp.route('/save', methods=['POST'])
def agregarEmpleado():
    data = request.get_json()
    nuevo_empleado = service.agregarEmpleado(data)
    return jsonify(nuevo_empleado.as_dict()), 201

# Endpoint para actualizar un empleado
@empleado_bp.route('/update/<int:id_empleado>', methods=['PUT'])
def actualizarEmpleado(id_empleado):
    data = request.get_json()
    empleado = service.actualizarEmpleado(id_empleado, data)
    if empleado:
        return jsonify(empleado.as_dict()), 200
    return jsonify({"error": "Empleado no encontrado"}), 404

# Endpoint para eliminar logicamente un empleado
@empleado_bp.route('/delete/<int:id_empleado>', methods=['PATCH'])
def eliminaLogicamenteEmpleado(id_empleado):
    empleado = service.eliminarLogicamenteEmpleado(id_empleado)
    if empleado:
        return jsonify({"exito": "Empleado eliminado logicamente"}), 200
    return jsonify({"error": "Empleado no encontrado"}), 404

# Endpoint para restaurar un empleado
@empleado_bp.route('/restore/<int:id_empleado>', methods=['PATCH'])
def restaurarEmpleado(id_empleado):
    empleado = service.restaurarEmpleado(id_empleado)
    if empleado:
        return jsonify({"exito": "Empleado restaurado"}), 200
    return jsonify({"error": "Empleado no encontrado"}), 404