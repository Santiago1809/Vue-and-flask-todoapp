from utils.db import db


class Tarea(db.Model):
    id_tarea = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nulleable=False)
    descripcion = db.Column(db.String(255), nulleable=False)
    id_grupo = db.Colum(db.Integer, db.ForeignKey('grupo.id_grupo'))

    def __init__(self, titulo, descripcion, id_grupo):
        self.titulo = titulo
        self.descripcion = descripcion
        self.id_grupo = id_grupo
