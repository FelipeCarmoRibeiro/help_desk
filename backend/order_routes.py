from fastapi import APIRouter 

order_router = APIRouter(
    prefix="/orders", tags=["Orders"])


#dominio.com/orders/lista

@order_router.get("/lista", summary="Lista todos os chamados", description="Retorna uma lista de todos os chamados cadastrados no sistema")
async def chamados():
    return {"message": "Lista de chamados"}
