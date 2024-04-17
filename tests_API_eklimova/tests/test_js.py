import allure


# @pytest.mark.parametrize('title', ['MY_Apple', '4'])
def test_create_publication(create_publication):
    data = {
        "name": 'MY_Apple',
        "data": {
            "year": 2022,
            "price": 2849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "12 TB"
        }
    }
    create_publication.create_new_publication(payload=data)
    create_publication.check_status_code_is_200()
    create_publication.check_title_is_(data['name'])


@allure.feature('Publication')
@allure.story('Get publication')
def test_get_by_id(post_id, get_publication):
    get_publication.get_by_id(post_id)
    get_publication.check_status_code_is_200()
    get_publication.check_that_id_is(post_id)
    get_publication.check_response_json_schema()


def test_delete_pub(post_id, delete_publication, get_publication):
    delete_publication.delete(post_id)
    delete_publication.check_status_code_is_200()
    get_publication.get_by_id(post_id)
    get_publication.check_status_code_is_404()


def test_put_pub(post_id, put_publication):
    put_payload = {
        "name": "MY_Apple MacBook Pro 16100",
        "data": {
            "year": 2014,
            "price": 4849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "120 TB"
        }
    }
    put_publication.send_put_request(post_id)
    put_publication.check_year_is_changed(put_payload['data']['year'])
    put_publication.check_price_is_changed(put_payload['data']['price'])
    put_publication.check_hard_disk_is_changed(put_payload['data']['Hard disk size'])


def test_patch_pub(post_id, patch_publication):
    patch_payload = {
        "name": "MY_Apple MacBook Pro 1610",
        "data": {
            "price": 5849.99
        }
    }
    patch_publication.send_patch_request(post_id)
    patch_publication.check_price_is_changed(patch_payload['data']['price'])
    patch_publication.check_name_is_changed(patch_payload['name'])
