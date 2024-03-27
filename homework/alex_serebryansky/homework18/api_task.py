import requests

main_url = "https://api.restful-api.dev/objects"
create_url = main_url + "/{}"


def create_object() -> int:
    data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2023,
            "price": 3680,
            "CPU model": "M2",
            "Hard disk size": "500 Gb"
        }
    }
    response = requests.post(main_url, json=data)
    assert response.status_code == 200
    return response.json()["id"]


def get_object_by_id(obj_id: int):
    response = requests.get(create_url.format(obj_id))
    assert response.status_code == 200
    print(response.json())


def change_object(obj_id: int):
    data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2022,
            "price": 2980,
            "CPU model": "M1",
            "Hard disk size": "500 Gb"
        }
    }
    response = requests.put(create_url.format(obj_id), json=data)
    assert response.status_code == 200
    print(response.json())


def change_objects_field(obj_id: int):
    data = {
        "data": {
            "price": 3280,
            "CPU model": "M2"
        }
    }
    response = requests.patch(create_url.format(obj_id), json=data)
    assert response.status_code == 200
    print(response.json())


def delete_object(obj_id: int):
    response = requests.delete(create_url.format(obj_id))
    assert response.status_code == 200
    print(response.json())


object_id = create_object()
get_object_by_id(object_id)
change_object(object_id)
change_objects_field(object_id)
delete_object(object_id)

