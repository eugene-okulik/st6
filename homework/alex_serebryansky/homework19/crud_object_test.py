import pytest

from homework.alex_serebryansky.homework18.api_task import ObjectRest
from homework.alex_serebryansky.homework19.KindOfObject import *
from homework.alex_serebryansky.homework19.ResponseMessage import ResponseMessages


@pytest.fixture(scope='session')
def start_end():
    print('\nStart test')
    yield
    print('\nEnd test')


@pytest.mark.title('Checking validation response schema')
@pytest.mark.author('alexs')
def test_validation_schemas_after_creating_object(start_end):
    object_rest = ObjectRest()
    data = object_rest.fill_data(ObjectName.MACBOOK_14_PRO, 2020, 1920,
                                 cpu_model=ObjectCPUModel.CPU_I7, hdd_size=ObjectHardDiskSize.SSD_500,
                                 color=ObjectColor.SILVER)

    resp = object_rest.create_object(data)
    object_rest.validate_json('object_data.json', resp)


@pytest.mark.title('Checking CRUD object\'s requests')
@pytest.mark.author('alexs')
def test_crud_object():
    object_rest = ObjectRest()
    data = object_rest.fill_data(ObjectName.MACBOOK_14_PRO, 2020, 1920,
                                 ObjectCPUModel.CPU_I7, ObjectHardDiskSize.SSD_500,
                                 ObjectColor.SILVER)
    new_obj = object_rest.create_object(data)
    object_id = new_obj['id']
    object_info = object_rest.get_object_by_id(object_id)
    print(object_info)

    new_data = object_rest.fill_data(ObjectName.MACBOOK_16_AIR, 2022, 2920,
                                     ObjectCPUModel.CPU_M3, ObjectHardDiskSize.SSD_1T,
                                     ObjectColor.GREY)
    object_info2 = object_rest.update_all_object_data(new_data, object_id) \
        .get_object_by_id(object_id)
    print(object_info2)

    print(object_info != object_info2)

    updated_data = object_rest.fill_data(year=2021, color=ObjectColor.BLUE)

    object_info3 = object_rest.update_object_data(updated_data, object_id) \
        .get_object_by_id(object_id)
    print(object_info3)

    object_rest.delete_object(object_id)
    resp = object_rest.get_object_by_id(object_id)
    print(resp)

