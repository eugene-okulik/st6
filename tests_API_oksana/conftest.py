import pytest
from tests_API_oksana.endpoints.create_publication import CreatePublication
from tests_API_oksana.endpoints.get_publication import GetPublication
from tests_API_oksana.endpoints.put_publication import PutPublication
from tests_API_oksana.endpoints.patch_publication import PatchPublication
from tests_API_oksana.endpoints.delete_publication import DeletePublication


@pytest.fixture()
def post_id():
    create_publication = CreatePublication()
    create_publication.create_new_publication()
    post_id = create_publication.response.json()['id']
    yield post_id
    obj = DeletePublication()
    obj.delete_publication(post_id=post_id)


@pytest.fixture()
def create_publication():
    return CreatePublication()


@pytest.fixture()
def get_publication():
    return GetPublication()


@pytest.fixture()
def put_publication():
    return PutPublication()


@pytest.fixture()
def patch_publication():
    return PatchPublication()


@pytest.fixture()
def delete_publication():
    return DeletePublication()
