#para rodar o servidor, use o comando: uvicorn main:app --reload

from passlib.context import CryptContext
from fastapi import FastAPI
from dotenv import load_dotenv
import os
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI(
    title="Help Desk API",
    description="API para gerenciamento de chamados",
    version="1.0.0"
)

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from order_routes import order_router
from auth_routes import auth_router

app.include_router(order_router)
app.include_router(auth_router)


