import requests


def create_object(load):
    response = requests.post('https://api.restful-api.dev/objects', json=load)
    return response.json()


def get_object_by_id(obj_ids):
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_ids}')
    return response.json()


def put_object_by_id(obj_ids, load):
    response = requests.put(f'https://api.restful-api.dev/objects/'
                            f'{obj_ids}', json=load)
    return response.json()


def patch_object_by_id(obj_ids, load):
    response = requests.patch(f'https://api.restful-api.dev/objects/'
                              f'{obj_ids}', json=load)
    return response.json()


def del_object_by_id(obj_ids):
    response = requests.delete(f'https://api.restful-api.dev/objects/'
                               f'{obj_ids}')
    return response.json()


payload = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}

obj = create_object(load=payload)
obj_id = obj['id']
print('result create_object: ', obj)

obj = get_object_by_id(obj_ids=obj_id)
obj_id = obj['id']
print('result get_object_by_id: ', obj)

payload = {
   "name": "Apple MacBook Pro 17",
   "data": {
      "year": 2024,
      "price": 1923,
      "CPU model": "Intel Core i11",
      "Hard disk size": "1.1 TB",
   }
}
obj = put_object_by_id(obj_ids=obj_id, load=payload)
obj_id = obj['id']
print('result put_object_by_id: ', obj)

payload = {
   "name": "Apple MacBook Pro 18"}
obj = patch_object_by_id(obj_ids=obj_id, load=payload)
obj_id = obj['id']
print('result patch_object_by_id: ', obj)

obj = del_object_by_id(obj_ids=obj_id)
print('result delete_object_by_id: ', obj)
