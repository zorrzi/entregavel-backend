from fastapi import APIRouter, Request, Response
from repositories.event_repository import EventRepository
from use_cases.director.update_event.update_event_use_case import UpdateEventUseCase

router = APIRouter()
event_repository = EventRepository()
update_event_use_case = UpdateEventUseCase(event_repository)

@router.put("/director/update-event/{event_id}")
def update_event(event_id: str, updated_fields: dict, response: Response, request: Request):
    return update_event_use_case.execute(event_id, updated_fields, response, request)
