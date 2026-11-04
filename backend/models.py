from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Configuração do banco de dados

db = create_engine("sqlite:///banco.db")

Base = declarative_base()
