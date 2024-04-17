import pytest
from tests_API_eklimova.endpoints.create_publication import CreatePublication
from tests_API_eklimova.endpoints.delete_publication import DeletePublication
from tests_API_eklimova.endpoints.get_publication import GetPublication
from tests_API_eklimova.endpoints.put_publication import PutPublication
from tests_API_eklimova.endpoints.patch_publication import PatchPublication


@pytest.fixture()
def post_id(create_publication):
    create_publication.create_new_publication()
    post_id = create_publication.response_json['id']
    yield post_id
    DeletePublication().delete(post_id)


@pytest.fixture()
def create_publication():
    return CreatePublication()


@pytest.fixture()
def get_publication():
    return GetPublication()


@pytest.fixture()
def delete_publication():
    return DeletePublication()


@pytest.fixture()
def put_publication():
    return PutPublication()


@pytest.fixture()
def patch_publication():
    return PatchPublication()
