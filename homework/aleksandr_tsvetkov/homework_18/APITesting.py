import requests


def post_req():
    data = {
        "name": "Google Pixel 9 Pro",
        "data": {
            "year": 2024,
            "price": 999.99,
            "CPU model": "Tensor G4",
            "Hard disk size": "512 Mb"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=data)
    obj_id = response.json()['id']
    if response.status_code == 200:
        print(response.json())
        return obj_id
    else:
        print(f'Ошибка {response.status_code} при создании объекта')
        return None


def get_req(obj_id):
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    print(f'Status code: {response.status_code}, {response.json()}')


# get_req(post_req())

def put_req(obj_id):
    data = {
        "name": "Google Pixel 9 Pro",
        "data": {
            "year": 2025,
            "price": 1200,
            "CPU model": "Tensor G5",
            "Hard disk size": "1024 Mb"
        }
    }
    response = requests.put(f'https://api.restful-api.dev/objects/{obj_id}', json=data)
    print(f'Status code: {response.status_code}, {response.json()}')


def patch_req(obj_id):
    data = {
        "name": "Google Pixel 9 Pro",
        "data": {
            "year": 2024,
        }
    }
    response = requests.patch(f'https://api.restful-api.dev/objects/{obj_id}', json=data)
    print(f'Status code: {response.status_code}, {response.json()}')


def delete_req(obj_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    print(response.json())


object_id = post_req()
get_req(object_id)
put_req(object_id)
patch_req(object_id)
delete_req(object_id)
