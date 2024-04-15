from pydantic import BaseModel, Field


class DataModel(BaseModel):
    year: int
    price: float
    CPU_model: str = Field(alias='CPU model')
    Hard_disk_size: str = Field(alias='Hard disk size')


class Publications(BaseModel):
    name: str
    data: DataModel


class DeleteModel(BaseModel):
    message: str
