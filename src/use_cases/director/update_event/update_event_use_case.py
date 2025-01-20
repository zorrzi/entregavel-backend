from repositories.event_repository import EventRepository
from fastapi import Request, Response

class UpdateEventUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def execute(self, event_id: str, updated_fields: dict, response: Response, request: Request):
        # Verifica se o evento existe
        event = self.event_repository.get_event_by_id(event_id)
        if not event:
            response.status_code = 404
            return {"status": "error", "message": "Evento não encontrado"}

        # Atualiza os campos fornecidos
        try:
            self.event_repository.update_event(event_id, updated_fields)
            response.status_code = 200
            return {"status": "success", "message": "Evento atualizado com sucesso"}
        except Exception as e:
            response.status_code = 500
            return {"status": "error", "message": f"Erro ao atualizar o evento: {str(e)}"}
