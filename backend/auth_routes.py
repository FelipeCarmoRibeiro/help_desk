from fastapi import APIRouter

auth_router = APIRouter(
    prefix="/auth", tags=["auth"]
)

@auth_router.get("/login", summary="Login", description="Endpoint para login de usuários")
async def login():
    return {"message": "Login endpoint"}