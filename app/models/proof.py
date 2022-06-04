from datetime import date
from pydantic import BaseModel

class ProofRequest(BaseModel):
    ProofDate: str
    Traits: str
    Animals: str