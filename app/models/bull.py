from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class Bull(BaseModel):
    Id: str = None
    RegId: str = None
    RegName: Optional[str] = None
    ShortName: Optional[str] = None
    Gender: str = None
    DateOfBirth: date = None
    IsDead: bool = None
    Breed: str = None
    BreedGroup: str = None
    Priority: int = None
    UpdateDate: datetime = None
