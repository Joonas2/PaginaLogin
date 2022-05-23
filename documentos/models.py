from documentos import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    nome_usuario = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False)
    senha = database.Column(database.String, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)

