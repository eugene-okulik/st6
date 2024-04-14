import pytest
import allure


@allure.feature("Create Object")
@allure.story("Post Request to Create an Object")
@allure.title("Test Create Object with POST Request")
def test_create_object(create_publication):
    payload = {
        "name": "Apple MacBook 22",
        "data": {
            "year": 2022,
            "price": 1883,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
        }
    }
    create_publication.create_new_publication(payload)
    create_publication.check_response_is_200()
    create_publication.check_name_is(name=payload['name'])
    create_publication.check_response_json_shema()


@allure.feature("Get Object")
@allure.story("Get Request to Retrieve Object by ID")
@allure.title("Test Update Object by ID with PUT Request")
@pytest.mark.critical
def test_get_object_by_id(post_id, get_publication):
    get_publication.get_by_id(post_id)
    get_publication.check_response_is_200()
    get_publication.check_id_is_correct(post_id)


@allure.feature("Update Object")
@allure.story("Put Request to Update an Object by ID")
@pytest.mark.parametrize('name', ['Apple MacBook Pro 16', 88], ids=['string', 'int'])
def test_put_object_by_id(name, post_id, put_publication):
    payload = {
        "name": name,
        "data": {
            "year": 2024,
            "price": 1923,
            "CPU model": "Intel Core i11",
            "Hard disk size": "1.1 TB",
        }
    }
    put_publication.put_obj_by_id(post_id=post_id, payload=payload)
    put_publication.check_name_is(name=payload['name'])
    put_publication.check_response_is_200()


@allure.feature("Modify Object")
@allure.story("Patch Request to Modify an Object by ID")
@pytest.mark.medium
def test_patch_object_by_id(post_id, patch_publication):
    payload = {
        "name": "Samsung"
    }

    patch_publication.patch_obj_by_id(post_id=post_id, payload=payload)
    patch_publication.validate_patch_response(expected_name=payload['name'])
    patch_publication.check_response_is_200()


@allure.feature("Delete Object")
@allure.story("Delete Request to Remove an Object by ID")
@allure.title("Test Delete Object by ID with DELETE Request")
def test_delete_post(post_id, get_publication, delete_publication):
    delete_publication.delete_publication(post_id)
    delete_publication.check_response_is_200()
    get_publication.get_by_id(post_id)
    get_publication.check_response_is_404()
