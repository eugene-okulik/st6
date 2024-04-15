from pydantic import BaseModel, Field


class DataModel(BaseModel):
    year: int
    price: int
    cpu_model: str = Field(alias='CPU model')
    disk_size: str = Field(alias='Hard disk size')


class PayloadModel(BaseModel):
    name: str
    data: DataModel
