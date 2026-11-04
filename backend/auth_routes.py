from fastapi import APIRouter, Depends
from models import User, db, Base
from sqlalchemy.orm import sessionmaker
from dependencies import get_sessao
from main import bcrypt_context


Base.metadata.create_all(bind=db)
auth_router = APIRouter(
    prefix="/auth", tags=["auth"]
)

@auth_router.get("/", summary="Página inicial", description="Retorna uma mensagem de boas-vindas")
async def home():
    return {"message": "Bem-vindo à página inicial"}


@auth_router.post("/register", summary="Cadastro de usuário", description="Realiza o cadastro de um novo usuário no sistema")
async def register(email: str, password: str, nome: str, session = Depends(get_sessao)):
    usuario = session.query(User).filter(User.email==email).first()
    if usuario:
        return {"message": "Usuário já cadastrado"}
    else:
        senha_secreta = bcrypt_context.hash(password)
        novo_usuario = User(nome, email, senha_secreta)
        session.add(novo_usuario)
        session.commit()
        return {"message": "Usuário cadastrado com sucesso"}
    
