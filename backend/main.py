#para rodar o servidor, use o comando: uvicorn main:app --reload


from fastapi import FastAPI

app = FastAPI(
    title="Help Desk API",
    description="API para gerenciamento de chamados",
    version="1.0.0"
)

from order_routes import order_router
from auth_routes import auth_router

app.include_router(order_router)
app.include_router(auth_router)


