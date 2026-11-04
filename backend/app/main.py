from fastapi import FastAPI

from app.database import engine, Base
from app.models import User, Ticket

from app.routers import users, tickets


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Help Desk API",
    description="API para gerenciamento de chamados",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(tickets.router)


@app.get("/")
def home():
    return {
        "message": "Bem-vindo à Help Desk API",
    }