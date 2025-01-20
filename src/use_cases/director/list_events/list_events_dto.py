from pydantic import BaseModel, Field

class ListEventsDTO(BaseModel):
    director_id: str = Field(..., description="ID do diretor para listar os eventos criados por ele")
