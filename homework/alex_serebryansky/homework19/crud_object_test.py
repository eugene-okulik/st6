import allure
import pytest
from hamcrest import assert_that, equal_to

from homework.alex_serebryansky.homework18.ObjectRest import ObjectRest, get_checks
from homework.alex_serebryansky.homework19 import ObjectPage
from homework.alex_serebryansky.homework19.TypeDataOfObject import *
from homework.alex_serebryansky.homework19.ResponseMessage import ResponseMessages, ResponseCodes
from homework.alex_serebryansky.homework19.object_features import *


@allure.title('Checking validation response schema after creating object')
@allure.story(CREATING_OBJECTS_STORY)
@allure.feature(VALIDATION_OBJECTS_SCHEMAS_FEATURE)
@pytest.mark.critical
@pytest.mark.author('alexs')
def test_validation_schemas_after_creating_object(start_end):
    object_rest = ObjectRest()
    data = object_rest.fill_data(ObjectName.MACBOOK_14_PRO, 2020, 1920,
                                 cpu_model=ObjectCPUModel.CPU_I7, hdd_size=ObjectHardDiskSize.SSD_500,
                                 color=ObjectColor.SILVER)

    resp = object_rest.create_object(data)
    object_rest.validate_json('object_data.json', resp)


@allure.title('Checking validation response schema after updating object (pydantic)')
@allure.story(UPDATING_OBJECTS_STORY)
@allure.feature(VALIDATION_OBJECTS_SCHEMAS_FEATURE)
@pytest.mark.medium
@pytest.mark.author('alexs')
def test_validation_schemas_after_updating_object(set_object_id_with_delete_object):
    object_rest = ObjectRest()
    data = object_rest.fill_data(ObjectName.MACBOOK_14_PRO, 2020, 1920,
                                 cpu_model=ObjectCPUModel.CPU_I7, hdd_size=ObjectHardDiskSize.SSD_500,
                                 color=ObjectColor.SILVER)

    resp = object_rest.update_all_object_data(data, set_object_id_with_delete_object)
    with allure.step('Checking validation response schema after updating object'):
        ObjectPage.ObjectBody(**resp)


@allure.title('Checking validation response schema after deleting object (pydantic)')
@allure.story(DELETING_OBJECTS_STORY)
@allure.feature(VALIDATION_OBJECTS_SCHEMAS_FEATURE)
@pytest.mark.medium
@pytest.mark.author('alexs')
def test_validation_schemas_after_updating_object(set_object_id_with_delete_object):
    object_rest = ObjectRest()
    resp = object_rest.delete_object(set_object_id_with_delete_object)
    with allure.step('Validating response schema after deleting object'):
        ObjectPage.ObjectAfterDeleting(**resp)


@allure.title('Checking CRUD object\'s requests')
@allure.story(CREATING_OBJECTS_STORY, UPDATING_OBJECTS_STORY, DELETING_OBJECTS_STORY)
@allure.feature(VALID_OBJECTS_VALUES_FEATURE)
@pytest.mark.critical
@pytest.mark.author('alexs')
def test_crud_object():
    object_rest = ObjectRest()
    data = object_rest.fill_data(ObjectName.MACBOOK_14_PRO, 2020, 1920,
                                 ObjectCPUModel.CPU_I7, ObjectHardDiskSize.SSD_500,
                                 ObjectColor.SILVER)
    object_id = object_rest.create_object(data)['id']
    object_info = object_rest.get_object_by_id(object_id)

    check1 = object_rest.check_values(object_info, object_id, data)

    new_data = object_rest.fill_data(ObjectName.MACBOOK_16_AIR, 2022, 2920,
                                     ObjectCPUModel.CPU_M3, ObjectHardDiskSize.SSD_1T,
                                     ObjectColor.GREY)
    object_rest.update_all_object_data(new_data, object_id)
    object_info2 = object_rest.get_object_by_id(object_id)

    check2 = object_rest.check_values(object_info2, object_id, new_data)

    updated_data = object_rest.fill_data(year=2021, color=ObjectColor.BLUE)
    object_rest.update_object_data(updated_data, object_id)
    object_info3 = object_rest.get_object_by_id(object_id)

    check3 = object_info2 != object_info3

    check4 = object_rest.delete_object(object_id)['message'] == ResponseMessages.OBJECT_HAS_DELETED.format(object_id)

    check5 = object_rest.get_object_by_id(object_id)['error'] == ResponseMessages.OBJECT_NOT_FOUND.format(object_id)

    assert_that(get_checks(locals()), equal_to(True))


@allure.title('Checking negative empty values in updated request')
@allure.story(UPDATING_OBJECTS_STORY)
@allure.feature(VALID_OBJECTS_VALUES_FEATURE)
@pytest.mark.critical
@pytest.mark.parametrize('name, year, price, cpu_model, hdd_size, color', [
    ({}, {}, {}, {}, {}, {}),
    ((), (), (), (), (), ()),
    ([], [], [], [], [], []), ],
                         ids=['empty dictionary', 'empty cortege', 'empty array', ])
@pytest.mark.author('alexs')
def test_check_empty_values_of_objects_data(start_end, set_object_id_with_delete_object,
                                            name, year, price, cpu_model,
                                            hdd_size, color):
    object_rest = ObjectRest()
    data = object_rest.fill_data(name, year, price, cpu_model, hdd_size, color)
    response = object_rest.update_all_object_data(data, set_object_id_with_delete_object, True)
    with allure.step('Verification status code of response'):
        assert response.status_code == ResponseCodes.BAD_REQUEST
