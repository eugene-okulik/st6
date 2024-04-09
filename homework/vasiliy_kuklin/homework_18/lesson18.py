import requests


def post_add_obj():
    payload = {
        "name": "Apple MacBook Pro 17",
        "data": {
            "year": 2024,
            "price": 2849.99,
            "CPU model": "Silicon m4",
            "Hard disk size": "10 TB"
        }
    }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.post('https://api.restful-api.dev/objects', json=payload, headers=headers)
    print(response.json())
    print(response.status_code)
    print(response.cookies)
    return response.json()


ids = 'ff8081818e9db438018eaaca246a424e'


def get_single_obj():
    response = requests.get(f'https://api.restful-api.dev/objects/{ids}')
    print(response.json())
    print(response.status_code)


def put_update_obj():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2017,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    headers = {
        'Content-type': 'application/json'
    }

    response = requests.put(f"https://api.restful-api.dev/objects/{ids}", json=payload, headers=headers)
    print(response.json())
    print(response.status_code)


def patch_part_update_obj():
    payload = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    headers = {
        'Content-type': 'application/json'
    }

    response = requests.patch(f'https://api.restful-api.dev/objects/{ids}', json=payload, headers=headers)
    print(response.json())
    print(response.status_code)


def delete_obj():
    response = requests.delete(f'https://api.restful-api.dev/objects/{ids}')
    print(response.json())
    print(response.status_code)
    print(response.cookies)


post_add_obj()
get_single_obj()
put_update_obj()
patch_part_update_obj()
delete_obj()
