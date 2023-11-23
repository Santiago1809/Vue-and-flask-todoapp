from flask import Flask
from utils.db import db
from routes.usuario import usuarios
from routes.grupo import grupo
from routes.tareas import tareas
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})
app.secret_key = "Secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://santiago:ryh89vw3Nr35Xru1l1kn5hL5FzsER7JI@dpg-clfldtvjc5ks73e88a00-a/vuenotes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(usuarios)
app.register_blueprint(grupo)
app.register_blueprint(tareas)
