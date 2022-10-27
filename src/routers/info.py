from pydantic import BaseModel


class DateRegionInfo(BaseModel):
    date: str
    region: str


class ResponseDustInfo(BaseModel):
    pm10: float
