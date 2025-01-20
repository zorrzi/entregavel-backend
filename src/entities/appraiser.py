import dotenv
from pydantic import BaseModel
from typing import Literal
dotenv.load_dotenv()

class Appraiser(BaseModel):
    _id: str
    name: str
    email: str
    password: str
    front: Literal["Business", "Engenharia", "Direito"]
    position: Literal["Consultor", "Liderança"]

    reset_pwd_token: str = ""
    reset_pwd_token_sent_at: int = 0