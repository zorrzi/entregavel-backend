from repositories.event_repository import EventRepository
from .create_event_dto import CreateEventDTO
from .create_event_use_case import CreateEventUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

create_event_use_case = CreateEventUseCase(EventRepository())

@router.post("/director/create-event")
def create_event(create_event_dto: CreateEventDTO, response: Response, request: Request):
    return create_event_use_case.execute(create_event_dto, response, request)
