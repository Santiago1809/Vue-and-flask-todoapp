from flask import Blueprint, request, jsonify
from models.Tarea import Tarea
from utils.db import db
from models.Grupo import Grupo

tareas = Blueprint('tareas', __name__)


@tareas.route('/tasks', methods=['GET'])
def obtener_tareas():
    id_grupo = request.args.get('id_grupo')
    tareas_bd = Tarea.query.filter_by(id_grupo=id_grupo)
    lista_tareas = [tarea.to_dict() for tarea in tareas_bd]
    return jsonify(lista_tareas)


@tareas.route('/create_task', methods=['POST'])
def crear_tarea():
    data = request.get_json()
    titulo = data['titulo']
    descripcion = data['descripcion']
    id_grupo = data['id_grupo']

    grupo = Grupo.query.get(id_grupo)
    if not grupo:
        return jsonify({'error': 'El grupo no existe'}),403

    nueva_tarea = Tarea(titulo, descripcion, id_grupo)

    try:
        db.session.add(nueva_tarea)
        db.session.commit()
        return nueva_tarea.to_dict()
    except Exception as e:
        return jsonify({'error': str(e)})
    
##TODO: Crear la lógica para eliminar y editar una tarea. Dentro de las opciones de edición se debe agregar la opción de cambiar una tarea de grupo