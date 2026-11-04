from models import db
from sqlalchemy.orm import Session, sessionmaker

def get_sessao():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()