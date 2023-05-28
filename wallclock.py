from pydantic import BaseModel


class Wallclock(BaseModel):
    id: int
    brand: str
    price: float
    shape: str