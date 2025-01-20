from fastapi import APIRouter, Request, Response
from repositories.event_repository import EventRepository
from use_cases.director.delete_event.delete_event_use_case import DeleteEventUseCase

router = APIRouter()
event_repository = EventRepository()
delete_event_use_case = DeleteEventUseCase(event_repository)

@router.delete("/director/delete-event/{event_id}")
def delete_event(event_id: str, response: Response, request: Request):
    return delete_event_use_case.execute(event_id, response, request)
