from fastapi import APIRouter, Depends, HTTPException

from dependencies import get_sessao
from sqlalchemy.orm import Session
from schemas import ChamadoSchema
from models import Chamado

order_router = APIRouter(
    prefix="/orders", tags=["Orders"])


#dominio.com/orders/lista

@order_router.get("/lista", summary="Lista todos os chamados", description="Retorna uma lista de todos os chamados cadastrados no sistema")
async def chamados():
    return {"message": "Lista de chamados"}

#dominio.com/orders/criar

@order_router.post("/criar", summary="Cria um novo chamado", description="Cria um novo chamado no sistema com base nas informações fornecidas")
async def criar_chamado(chamado_schema: ChamadoSchema, session: Session = Depends(get_sessao)):
    new_chamado = Chamado(titulo=chamado_schema.titulo, descricao=chamado_schema.descricao, status=chamado_schema.status, usuario=chamado_schema.id_usuario)
    session.add(new_chamado)
    session.commit()
    if not chamado_schema.titulo or not chamado_schema.descricao:
        raise HTTPException(status_code=400, detail="Titulo e descrição obrigatórios")
    return {"message": f"Chamado criado com sucesso {new_chamado.id}"}
