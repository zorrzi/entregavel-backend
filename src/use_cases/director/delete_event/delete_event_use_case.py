from repositories.event_repository import EventRepository
from fastapi import Request, Response

class DeleteEventUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def execute(self, event_id: str, response: Response, request: Request):


        event = self.event_repository.get_event_by_id(event_id)
        if not event:
            response.status_code = 404
            return {"status": "error", "message": "Evento não encontrado"}

        try:
            self.event_repository.delete_event(event_id)
            response.status_code = 200
            return {"status": "success", "message": "Evento excluído com sucesso"}
        except Exception as e:
            response.status_code = 500
            return {"status": "error", "message": f"Erro ao excluir o evento: {str(e)}"}
