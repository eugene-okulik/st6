import requests


def create_obj():
    body = {
        "name": "Test me",
        "data": {
            "year": 2024,
            "price": 11.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post("https://api.restful-api.dev//objects", json=body).json()
    print(response)


def get_obj_lists():
    response = (requests.get("https://api.restful-api.dev/objects")).json()
    print(response)


def get_obj_by_id():
    response = (requests.get("https://api.restful-api.dev/objects?id=ff8081818e21ce2d018e85cf6dbf732c"))
    print(response.json())


def change_obj():
    body = {
        "name": "TEST ME UPD",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "gold"
        }
    }
    response = requests.put("https://api.restful-api.dev/objects/ff8081818e21ce2d018e85c961b17327", json=body)
    print(response.json())


def change_obj_partially():
    body = {
        "name": "TEST ME UPD again",
    }
    response = requests.patch("https://api.restful-api.dev/objects/ff8081818e21ce2d018e85d98cc67336", json=body)
    print(response.json())


def delete_obj():
    response = requests.delete("https://api.restful-api.dev/objects/ff8081818e21ce2d018e85c961b17327")
    print(response.json())


# create_obj()
# get_obj_lists()
# get_obj_by_id()
# change_obj()
change_obj_partially()
# delete_obj()
