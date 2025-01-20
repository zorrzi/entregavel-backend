from repositories.event_repository import EventRepository
from use_cases.director.create_event.create_event_dto import CreateEventDTO
from fastapi import Request, Response
from entities.event import Event

class CreateEventUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def execute(self, create_event_dto: CreateEventDTO, response: Response, request: Request):
        # Validação de campos obrigatórios
        if (
            not create_event_dto.name
            or not create_event_dto.date
            or not create_event_dto.location
            or not create_event_dto.capacity
            or not create_event_dto.start_time
            or not create_event_dto.end_time
        ):
            response.status_code = 400
            return {"status": "error", "message": "Faltam informações obrigatórias para criar o evento."}

        # Cria o objeto do evento
        event = Event(
            _id="",
            name=create_event_dto.name,
            description=create_event_dto.description,
            date=create_event_dto.date,
            location=create_event_dto.location,
            capacity=create_event_dto.capacity,
            start_time=create_event_dto.start_time,
            end_time=create_event_dto.end_time,
            participants=[]
        )

        # Salva o evento no repositório
        try:
            self.event_repository.save(event)
            response.status_code = 201
            return {"status": "success", "message": "Evento criado com sucesso."}
        except Exception as e:
            response.status_code = 500
            return {"status": "error", "message": f"Erro ao salvar o evento: {str(e)}"}
