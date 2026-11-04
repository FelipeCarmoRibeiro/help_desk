from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class TicketCreate(BaseModel):
    title: str
    description: str
    category: str
    priority: str = "normal"


class TicketUpdate(BaseModel):
    status: Optional[str] = None
    priority: Optional[str] = None


class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    category: str
    priority: str
    status: str
    user_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)