import requests


def get_reqs():
    cookies = {'enwiki_session': '17ab96bd8ffbe8ca58a78657a918558'}
    response = requests.get('https://jsonplaceholder.typicode.com/posts', cookies=cookies)
    result = response.json()
    for x in result:
        print(x)
    print(response.status_code)

    response = requests.get('https://jsonplaceholder.typicode.com/posts/42')
    print(response.json())


def post_req():
    payload = {
        "title": "My title",
        "Body": "My publication content",
        "userId": 1
    }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload, headers=headers)
    print(response.json())
    print(response.status_code)
    print(response.cookies)


def put_req():
    payload = {
        "title": "My title-UPD",
        "Body": "My publication content-UPD",
        "userId": 1
    }
    headers = {
        'Content-type': 'application/json'
    }

    response = requests.put('https://jsonplaceholder.typicode.com/posts/42', json=payload, headers=headers)
    print(response.json())
    print(response.status_code)


def patch_req():
    payload = {
        "title": "My title-UPD"
    }
    headers = {
        'Content-type': 'application/json'
    }

    response = requests.patch('https://jsonplaceholder.typicode.com/posts/42', json=payload, headers=headers)
    print(response.json())
    print(response.status_code)


def delete_req():
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/42')
    print(response.json())
    print(response.status_code)
    print(response.cookies)


# post_req()
