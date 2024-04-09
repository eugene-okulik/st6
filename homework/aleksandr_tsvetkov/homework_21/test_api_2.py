import pytest
import requests
import allure


@pytest.fixture(scope='session', autouse=True)
def setup_and_teardown():
    print('\nStart Testing')
    yield
    print('\nTesting completed')


@pytest.fixture()
def obj_id():
    payload = {
        "name": "ASUS ROG GH70",
        "data": {
            "year": 2007,
            "price": 1099.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=payload)
    obj_id = response.json()['id']
    yield obj_id
    requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')


@allure.tag('Smoke')
@allure.title('Checking the creation of a product object with specified characteristics')
@allure.story('Create product')
@allure.feature('Publication')
def test_create_obj():
    with allure.step('Send POST request'):
        payload = {
            "name": "ASUS ROG GH70",
            "data": {
                "year": 207,
                "price": 1099.99,
                "CPU model": "Intel Core i7",
                "Hard disk size": "1 TB"
            }
        }
    response = requests.post('https://api.restful-api.dev/objects', json=payload)
    with allure.step('Checking that status code is 200'):
        assert response.status_code == 200, 'Status code is not Ok'
    with allure.step('Checking if the values match'):
        assert response.json()['name'] == payload['name'] and response.json()['data'] == payload['data'], \
            'The values don\'t match'


@allure.tag('Smoke')
@allure.story('Product search by id')
@allure.feature('Publication')
def test_get_obj_by_id(obj_id):
    with allure.step('Send GET request'):
        response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    with allure.step('Checking that status code is 200'):
        assert response.status_code == 200, 'Status code is not Ok'
    with allure.step('check that the product id in the response is equal to the product id in the request'):
        assert response.json()['id'] == obj_id, 'Object ID don\'t match'


@allure.tag('Regression')
@allure.title('Complete product change')
@allure.story('Product change')
@allure.feature('Publication')
def test_put_obj(obj_id):
    with allure.step('Send PUT request'):
        payload = {
            "name": "ASUS ROG GH71",
            "data": {
                "year": 2008,
                "price": 1199.99,
                "CPU model": "Intel Core i3",
                "Hard disk size": "512MB"
            }
        }
    response = requests.put(f'https://api.restful-api.dev/objects/{obj_id}', json=payload)
    with allure.step('Checking that status code is 200'):
        assert response.status_code == 200, 'Status code is not Ok'
    with allure.step('Checking if the values match'):
        assert response.json()['name'] == payload['name'] and response.json()['data'] == payload['data'], \
            'The values don\'t match'


@allure.tag('Smoke')
@allure.title('Product edit')
@allure.story('Product edit')
@allure.feature('Publication')
def test_patch_obj(obj_id):
    with allure.step('Send PATCH request'):
        payload = {
            'data': {
                'year': 2007
            }
        }
    response = requests.patch(f'https://api.restful-api.dev/objects/{obj_id}', json=payload)
    with allure.step('Checking that status code is 200'):
        assert response.status_code == 200, 'Status code is not Ok'
    with allure.step('Checking if the values match'):
        assert response.json()['data'] == payload['data'], 'The values don\'t match'


@allure.tag('Regression')
@allure.title('Product delete')
@allure.story('Product delete')
@allure.feature('Publication')
def test_delete_obj(obj_id):
    with allure.step('Send DELETE request'):
        response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    with allure.step('Checking that status code is 200'):
        assert response.status_code == 200, 'Status code is not Ok'
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    with allure.step('Checking that status code is 404'):
        assert response.status_code == 404, 'Object still exists after deletion'
