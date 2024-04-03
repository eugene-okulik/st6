import pytest
import requests
from pydantic import BaseModel, Field
from typing import Any


class Publication(BaseModel):
    userId: int
    id: int
    title: str
    body: int


@pytest.mark.smoke
@pytest.mark.parametrize('title', ['My title', 45, [2, 5]], ids=['string', 'int', 'array'])
def test_create_publication_string(title):
    payload = {
        "title": title,
        "Body": "My publication content",
        "userId": 1
    }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload, headers=headers)
    assert response.status_code == 201, 'Status code is not Ok'
    assert response.json()['title'] == payload['title'], 'Invalid title'


@pytest.mark.new_feature
def test_get_by_id(post_id):
    post_id = 42
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    assert response.status_code == 200, 'Status code is not Ok'
    assert response.json()['id'] == post_id, 'Id is not correct'
    Publication(**response.json())


class NewObj(BaseModel):
    id: str
    name: str
    data: dict[str, Any]


class ObjectData(BaseModel):
    color: str
    capacity_GB: int = Field(alias='capacity GB')


class NewObjWithObj(BaseModel):
    id: str
    name: str
    data: ObjectData
    here: int = None


def test_hw():
    response = requests.get('https://api.restful-api.dev/objects/3').json()
    NewObj(**response)
    NewObjWithObj(**response)


def test_here():
    data = {
        "id": "3",
        "name": "Apple iPhone 12 Pro Max",
        "data": {
            "color": "Cloudy White",
            "capacity GB": 512
        },
        "here": "ksdjfhs"
    }
    NewObjWithObj(**data)
