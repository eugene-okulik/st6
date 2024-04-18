from pydantic import BaseModel, Field


class ObjectData(BaseModel):
    year: int
    price: float
    CPU_model: str = Field(alias='CPU model')
    Hard_disk_size: str = Field(alias='Hard disk size')


class Object(BaseModel):
    id: str
    name: str
    data: ObjectData
    createdAt: str
