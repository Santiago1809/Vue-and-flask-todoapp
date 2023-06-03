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
    
@tareas.route('/update_task', methods=['POST'])
def actualizar_tarea():
    data = request.get_json()
    id_tarea = data['id_tarea']
    titulo = data['titulo']
    descripcion = data['descripcion']
    id_grupo = data['id_grupo']

    tarea_ac = Tarea.query.get(id_tarea)  # Utiliza el método get() en lugar de filter()

    if tarea_ac:
        try:
            tarea_ac.titulo = titulo
            tarea_ac.descripcion = descripcion
            tarea_ac.id_grupo = id_grupo
            db.session.commit()  # Guarda los cambios en la base de datos
            return tarea_ac.to_dict()
        except Exception as e:
            return jsonify({'error': str(e)})
    else:
        return jsonify({'error': 'La tarea no existe.'})
    

@tareas.route('/delete_task', methods=['DELETE'])
def eliminar_tarea():
    id_tarea = request.args.get('id_tarea')
    tarea_eliminar = Tarea.query.get(id_tarea)
    try:
        db.session.delete(tarea_eliminar)
        db.session.commit()
        return jsonify({'mensaje':'Tarea eliminada'})
    except Exception as e:
        return jsonify({'error': str(e)})