from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils.types import ChoiceType
import os
# Configuração do banco de dados




from sqlalchemy import create_engine

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_URL = "sqlite:///" + os.path.join(BASE_DIR, "banco.db")

db = create_engine(DATABASE_URL)

Base = declarative_base()


# usuarios
class User(Base):
    __tablename__ = "users"

    id = Column("id",Integer, nullable=False, primary_key=True, autoincrement=True)
    nome = Column("name",String)
    email = Column("email",String, nullable=False, unique=True)
    senha = Column("password",String)
    ativo = Column("active",Boolean)
    admin = Column("admin",Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


#chamados
class Chamado(Base):
    __tablename__ = "chamados"

 #   STATUS_CHAMADO = (
  #      ("Aberto", "Aberto"),
   #     ("EmAndamento", "Em Andamento"),
    #
    #     ("Fechado", "Fechado")
    #)

    id = Column("id",Integer, nullable=False, primary_key=True, autoincrement=True)
    titulo = Column("title",String)
    descricao = Column("description",String)
    status = Column("status",String, default="Aberto")
    usuario = Column("user_chamado",Integer, ForeignKey("users.id"))


    def __init__(self, titulo, descricao, status="Aberto", usuario=None):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.usuario = usuario


print("Caminho do banco:", DATABASE_URL)
print("Pasta existe:", os.path.exists(BASE_DIR))
print("Banco existe:", os.path.exists(os.path.join(BASE_DIR, "banco.db")))