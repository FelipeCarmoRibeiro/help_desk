from pydantic import BaseModel
from typing import Optional

class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool] 
    admin: Optional[bool] 
    class Config:
        from_attributes = True

    


class ChamadoSchema(BaseModel):
    id: int
    titulo: str
    descricao: str
    status: Optional[bool] 
    id_usuario: Optional[int]
    

    class Config:
        from_attributes = True