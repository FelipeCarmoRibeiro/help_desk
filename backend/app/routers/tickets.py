from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.models.ticket import Ticket
from app.schemas.ticket import (
    TicketCreate,
    TicketUpdate,
    TicketResponse
)

from app.core.dependencies import (
    get_current_user,
    get_admin_user
)


router = APIRouter(
    prefix="/tickets",
    tags=["Chamados"]
)


# CRIAR CHAMADO
@router.post("/", response_model=TicketResponse, status_code=201)
def create_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    if ticket.priority not in ["baixa", "normal", "alta"]:
        raise HTTPException(
            status_code=400,
            detail="Prioridade inválida"
        )

    new_ticket = Ticket(
        title=ticket.title,
        description=ticket.description,
        category=ticket.category,
        priority=ticket.priority,
        user_id=current_user.id
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return new_ticket


# LISTAR MEUS CHAMADOS
@router.get("/my", response_model=list[TicketResponse])
def my_tickets(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return db.query(Ticket).filter(
        Ticket.user_id == current_user.id
    ).all()


# LISTAR TODOS OS CHAMADOS (ADMIN)
@router.get("/admin/all", response_model=list[TicketResponse])
def all_tickets(
    db: Session = Depends(get_db),
    admin: User = Depends(get_admin_user)
):

    return db.query(Ticket).all()


# ATUALIZAR CHAMADO (ADMIN)
@router.patch("/{ticket_id}", response_model=TicketResponse)
def update_ticket(
    ticket_id: int,
    ticket_data: TicketUpdate,
    db: Session = Depends(get_db),
    admin: User = Depends(get_admin_user)
):

    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Chamado não encontrado"
        )

    if ticket_data.status is not None:
        if ticket_data.status not in [
            "aberto", "em andamento", "resolvido", "fechado"
        ]:
            raise HTTPException(
                status_code=400,
                detail="Status inválido"
            )

        ticket.status = ticket_data.status

    if ticket_data.priority is not None:
        if ticket_data.priority not in [
            "baixa", "normal", "alta"
        ]:
            raise HTTPException(
                status_code=400,
                detail="Prioridade inválida"
            )

        ticket.priority = ticket_data.priority

    db.commit()
    db.refresh(ticket)

    return ticket


# VISUALIZAR UM CHAMADO
@router.get("/{ticket_id}", response_model=TicketResponse)
def get_ticket(
    ticket_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Chamado não encontrado"
        )

    if (
        ticket.user_id != current_user.id
        and current_user.role != "admin"
    ):
        raise HTTPException(
            status_code=403,
            detail="Você não tem permissão para visualizar este chamado"
        )

    return ticket