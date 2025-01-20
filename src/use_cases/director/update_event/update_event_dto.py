from pydantic import BaseModel, Field
from typing import Optional

class UpdateEventDTO(BaseModel):
    event_id: str = Field(..., description="ID do evento a ser atualizado")
    name: Optional[str] = Field(None, description="Novo nome do evento")
    description: Optional[str] = Field(None, description="Nova descrição do evento")
    dia: Optional[str] = Field(None, description="Novo dia do evento")
    mes: Optional[str] = Field(None, description="Novo mês do evento")
    ano: Optional[str] = Field(None, description="Novo ano do evento")
    location: Optional[str] = Field(None, description="Novo local do evento")
    capacity: Optional[int] = Field(None, description="Nova capacidade do evento")
    start_time: Optional[str] = Field(None, description="Novo horário de início")
    end_time: Optional[str] = Field(None, description="Novo horário de término")
