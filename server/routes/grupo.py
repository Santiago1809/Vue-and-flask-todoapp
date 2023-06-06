from flask import Blueprint, request, jsonify
from models.Grupo import Grupo
from utils.db import db
from models.Tarea import Tarea

grupo = Blueprint('Grupo', __name__)


@grupo.route('/groups', methods=['GET'])
def groups():
    id_usuario = request.args.get('id_usuario')
    grupos = Grupo.query.filter_by(id_usuario=id_usuario).all()

    grupos_serializables = [grupo.to_dict() for grupo in grupos]

    return jsonify(grupos_serializables)


@grupo.route('/group', methods=['GET'])
def group():
    id_grupo = request.args.get('id_grupo')
    grupo = Grupo.query.get(id_grupo)

    return jsonify({'Grupo': grupo.to_dict()})


@grupo.route('/create_group', methods=['POST'])
def create_group():
    data = request.get_json()
    id_usuario = data['id_usuario']
    nombre = data['nombre_grupo']
    nuevo_grupo = Grupo(id_usuario, nombre)
    db.session.add(nuevo_grupo)
    try:
        db.session.commit()
        grupos_bd = Grupo.query.all()
        return jsonify({'Grupos': grupo.to_dict() for grupo in grupos_bd})
    except Exception as e:
        return jsonify({'error': str(e)}), 408


@grupo.route('/delete_group', methods=['DELETE'])
def delete_group():
    try:
        data = request.get_json()
        id_grupo = data['id_grupo']
        grupo = Grupo.query.get(id_grupo)

        if grupo:
            Tarea.query.filter_by(id_grupo=id_grupo).delete()
            db.session.delete(grupo)
            db.session.commit()
            return jsonify({'message': 'Grupo eliminado correctamente'})
        else:
            return jsonify({'error': 'Grupo no encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@grupo.route('/edit_group', methods=['PUT'])
def editar_grupo():
    try:
        data = request.get_json()
        id_grupo = data['id_grupo']
        nuevo_nombre = data['nombre_grupo']
        grupo = Grupo.query.get(id_grupo)

        if grupo:
            grupo.nombre_grupo = nuevo_nombre
            db.session.commit()
            return jsonify({'message': 'Grupo actualizado correctamente'})
        else:
            return jsonify({'error': 'Grupo no encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
