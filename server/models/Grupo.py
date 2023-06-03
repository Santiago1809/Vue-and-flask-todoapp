from utils.db import db


class Grupo(db.Model):
    id_grupo = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    nombre_grupo = db.Column(db.String(255), nullable=False)

    def __init__(self, id_usuario, nombre_grupo):
        self.id_usuario = id_usuario
        self.nombre_grupo = nombre_grupo

    def to_dict(self):
        return {
            'id_grupo': self.id_grupo,
            'nombre': self.nombre_grupo
        }
