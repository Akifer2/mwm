from pydantic import BaseModel, Field

class VehicleIn(BaseModel):
    plate: str = Field(max_length=10)
    brand: str
    model: str
    year:  int
    color: str = Field(max_length=50)

class VehicleOut(VehicleIn):
    id: int

    class Config:
        orm_mode = True
