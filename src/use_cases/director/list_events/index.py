from fastapi import APIRouter, Response, Request
from repositories.event_repository import EventRepository
from use_cases.director.list_events.list_events_use_case import ListEventsUseCase
from use_cases.director.list_events.list_events_dto import ListEventsDTO

router = APIRouter()
event_repository = EventRepository()
list_events_use_case = ListEventsUseCase(event_repository)

@router.get("/director/list-events")
def list_events(director_id: str, response: Response, request: Request):
    dto = ListEventsDTO(director_id=director_id)
    return list_events_use_case.execute(dto, response, request)
