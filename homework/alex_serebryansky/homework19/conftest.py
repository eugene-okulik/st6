import pytest
import requests

from homework.alex_serebryansky.homework18.ObjectRest import ObjectRest


@pytest.fixture(scope='session')
def start_end():
    print('\nStart test')
    yield
    print('\nEnd test')


@pytest.fixture(scope='session')
def set_object_id_with_delete_object():
    test_object = ObjectRest()
    test_object_data = test_object.fill_data()
    test_object_id = test_object.create_object(test_object_data)['id']
    yield test_object_id
    test_object.delete_object(test_object_id)


@pytest.fixture(scope='session')
def set_object_id():
    test_object = ObjectRest()
    test_object_data = test_object.fill_data()
    object_id = test_object.create_object(test_object_data)['id']
    return object_id
