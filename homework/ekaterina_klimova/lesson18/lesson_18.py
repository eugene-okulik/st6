import requests


# Создание объекта
def post_method(data):

    new_rec = requests.post("https://api.restful-api.dev/objects", json=data)
    print(new_rec.json())
    print(new_rec.status_code)


new_line = {
    "name": "MY_Apple MacBook Pro 16100",
    "data": {
        "year": 2022,
        "price": 2849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "12 TB"
    }
}

post_method(new_line)


# Получение объекта по его id
def get_info(id_object):
    responce = requests.get(f"https://api.restful-api.dev/objects?id={id_object}")
    print(responce.status_code)
    print(responce.json())


id_obj = 'ff8081818e21ce2d018e801b9dca6b6b'
get_info(id_obj)


# Изменение объекта с помощью метода PUT
def put_obj(id_object, data):
    request = requests.put(f"https://api.restful-api.dev/objects/{id_object}", json=data)
    print(request.status_code)
    print(request.json())


put_payload = {
    "name": "MY_Apple MacBook Pro 16100",
    "data": {
        "year": 2024,
        "price": 4849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "120 TB"
    }
}

put_obj(id_obj, put_payload)


# Изменение объекта с помощью метода PATCH
def patch_obj(id_object, data):
    request = requests.patch(f"https://api.restful-api.dev/objects/{id_object}", json=data)
    print(request.status_code)
    print(request.json())


patch_payload = {
    "name": "MY_Apple MacBook Pro 1610",
    "data": {
        "price": 5849.99
    }
}
patch_obj(id_obj, patch_payload)


# Удаление объекта
def delete_obj(id_object):
    request = requests.delete(f"https://api.restful-api.dev/objects/{id_object}")
    print(request.status_code)
    print(request.json())


delete_obj(id_obj)
