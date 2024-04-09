from pydantic import BaseModel


class ObjectData(BaseModel):
    price: int
    cpu_model: str = None
    hdd_size: str = None
    color: str = None


class ObjectBody(BaseModel):
    name: str
    id: str
    created_at: str
    data: ObjectData


class ObjectAfterDeleting(BaseModel):
    message: str
