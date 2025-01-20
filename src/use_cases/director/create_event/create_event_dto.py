from pydantic import BaseModel, Field
from typing import Optional, List

class CreateEventDTO(BaseModel):
    name: str = Field(..., description="Nome do evento")
    description: Optional[str] = Field("Evento sem descrição", description="Descrição do evento")
    date: str = Field(..., description="Data do evento no formato YYYY-MM-DD")
    location: str = Field(..., description="Local do evento")
    capacity: int = Field(..., description="Capacidade do evento")
    start_time: str = Field(..., description="Horário de início do evento")
    end_time: str = Field(..., description="Horário de término do evento")
