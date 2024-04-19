import pytest
from tests_API_vkuklin.endpoints.create_object import CreateObject
from tests_API_vkuklin.endpoints.delete_object import DeleteObject
from tests_API_vkuklin.endpoints.get_object import GetObject
from tests_API_vkuklin.endpoints.update_object import UpdateObject
from tests_API_vkuklin.endpoints.patch_object import PatchObject


@pytest.fixture()
def object_id(create_object):
    create_object.create_new_object()
    object_id = create_object.response_json['id']
    yield object_id
    DeleteObject().delete(object_id)


@pytest.fixture()
def create_object():
    return CreateObject()


@pytest.fixture()
def get_object():
    return GetObject()


@pytest.fixture()
def update_object():
    return UpdateObject()


@pytest.fixture()
def patch_object():
    return PatchObject()


@pytest.fixture()
def delete_object():
    return DeleteObject()
