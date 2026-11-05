from fastapi import APIRouter, Depends, HTTPException
from models import User, db, Base
from dependencies import get_sessao
from main import bcrypt_context
from schemas import UsuarioSchema
from sqlalchemy.orm import Session


Base.metadata.create_all(bind=db)
auth_router = APIRouter(
    prefix="/auth", tags=["auth"]
)
#dominio.com/auth
@auth_router.get("/", summary="Página inicial", description="Retorna uma mensagem de boas-vindas")
async def home():
    return {"message": "Bem-vindo à página inicial"}

#dominio.com/auth/register
@auth_router.post("/register", summary="Cadastro de usuário", description="Realiza o cadastro de um novo usuário no sistema")
async def register(usuario_schema: UsuarioSchema, session: Session = Depends(get_sessao)):
    usuario = session.query(User).filter(User.email==usuario_schema.email).first()
    if usuario:
        raise HTTPException(status_code=400, detail="Usuário já cadastrado")
    else:
        senha_secreta = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = User(usuario_schema.nome, usuario_schema.email, senha_secreta, usuario_schema.ativo, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {"message": f"Usuário cadastrado com sucesso {usuario_schema.email}"}
    
