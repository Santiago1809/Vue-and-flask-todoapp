from flask import Blueprint, request, jsonify
from models.Usuario import Usuario
from utils.db import db
import bcrypt

usuarios = Blueprint('usuarios', __name__)


@usuarios.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    nombre = data['nombre']
    correo = data['correo']
    contraseñaFormulario = data['contraseña']

    # Verificar si el correo ya existe en la base de datos
    usuario_existente = Usuario.query.filter_by(correo=correo).first()
    if usuario_existente:
        return jsonify({'register': 0}), 409

    # Hash de la contraseña
    contraseña = bcrypt.hashpw(contraseñaFormulario.encode('utf-8'), bcrypt.gensalt())

    nuevo_usuario = Usuario(nombre, correo, contraseña)
    try:
        db.session.add(nuevo_usuario)
        db.session.commit()
        return jsonify({'register': 1}, {'usuario': nuevo_usuario.to_dict()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@usuarios.route("/login", methods=['POST'])
def login():
    if request.method == "POST":
        data = request.get_json()
        correo = data['correo']
        contraseñaRecibida = data['contraseña']
        usuario = Usuario.query.filter_by(correo=correo).first()

        if usuario and bcrypt.checkpw(contraseñaRecibida.encode('utf8'), usuario.contraseña.encode('utf8')):
            return jsonify({'access': 'allowed'}, {'usuario': usuario.to_dict()} )
        else:
            return jsonify({'access': 'denied'})
