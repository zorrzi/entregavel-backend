from repositories.event_repository import EventRepository
from use_cases.director.list_events.list_events_dto import ListEventsDTO
from fastapi import Response, Request

class ListEventsUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def execute(self, list_events_dto: ListEventsDTO, response: Response, request: Request):
        # Buscar eventos criados pelo diretor
        events = self.event_repository.get_events_by_director(list_events_dto.director_id)
        if not events:
            response.status_code = 404
            return {"status": "error", "message": "Nenhum evento encontrado para este diretor"}

        # Retornar os eventos encontrados
        response.status_code = 200
        return {"status": "success", "events": events}
