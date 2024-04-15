import allure
import pytest
from test_API_volha.conftest import *


@allure.feature('Create booking')
@allure.suite('CRUD with bookings')
@pytest.mark.critical
def test_create_booking(start_end, create_booking, delete_booking_by_id, get_auth_token):
    create_booking.create_booking()

    create_booking.check_resp_code_is_200()
    create_booking.check_response_schema()

    get_auth_token.get_auth_token()
    delete_booking_by_id.delete_booking(booking_id=create_booking.booking_id, token=get_auth_token.token)


@allure.suite('CRUD with bookings')
@allure.feature('GET booking')
@allure.story('Get booking by id')
def test_get_booking_by_id(start_end, create_booking, get_booking_by_id, get_auth_token, delete_booking_by_id):
    create_booking.create_booking()
    booking_id = create_booking.booking_id
    first_name_post = create_booking.first_name
    price_post = create_booking.total_price

    get_booking_by_id.get_booking_by_id(booking_id)

    get_booking_by_id.check_resp_code_is_200()
    get_booking_by_id.check_total_price_is_(price_post)
    get_booking_by_id.check_first_name_is_(first_name_post)
    get_booking_by_id.check_response_schema()

    get_auth_token.get_auth_token()

    delete_booking_by_id.delete_booking(booking_id=booking_id, token=get_auth_token.token)


@allure.suite('CRUD with bookings')
@allure.feature('UPDATE booking')
@allure.story('Update booking FULL')
@pytest.mark.parametrize("firstname, totalprice, checkin",
                         [("Bill", 45, "2019-01-02"),
                          ("Mark", 88, "2019-01-05"),
                          ("Simon", 120, "2019-01-03")])
def test_update_booking_full(start_end, create_booking, get_auth_token, update_booking_full,
                             delete_booking_by_id, firstname, totalprice, checkin):
    create_booking.create_booking()
    booking_id = create_booking.booking_id

    upd_body = {
        "firstname": firstname,
        "lastname": "Brown",
        "totalprice": totalprice,
        "depositpaid": True,
        "bookingdates": {
            "checkin": checkin,
            "checkout": "2019-01-30"
        },
        "additionalneeds": "Breakfast"
    }

    get_auth_token.get_auth_token()

    update_booking_full.update_booking_full(booking_id=booking_id, token=get_auth_token.token, body=upd_body)

    update_booking_full.check_resp_code_is_200()
    update_booking_full.check_first_name_is_(firstname)
    update_booking_full.check_total_price_is_(totalprice)
    update_booking_full.check_booking_dates_checkin(checkin)

    delete_booking_by_id.delete_booking(booking_id=booking_id, token=get_auth_token.token)


@allure.suite('CRUD with bookings')
@allure.feature('UPDATE booking')
@allure.story('Update user booking')
@pytest.mark.parametrize("lastname, additionalneeds",
                         [('Hense', 'Fan in the room'),
                          ('Rimma', 'Do not disturb')])
def test_update_booking_partially(start_end, create_booking, get_auth_token, delete_booking_by_id,
                                  update_booking_part, lastname, additionalneeds):
    create_booking.create_booking()
    booking_id = create_booking.booking_id

    upd_body = {
        "lastname": lastname,
        "additionalneeds": additionalneeds
    }

    get_auth_token.get_auth_token()

    update_booking_part.update_booking_partionally(booking_id=booking_id, token=get_auth_token.token, body=upd_body)

    update_booking_part.check_resp_code_is_200()
    update_booking_part.check_last_name_is_(lastname)
    update_booking_part.check_additional_needs_is_(additionalneeds)

    delete_booking_by_id.delete_booking(booking_id=booking_id, token=get_auth_token.token)


@allure.suite('CRUD with bookings')
@allure.feature('DELETE booking')
@allure.story('Delete booking')
@pytest.mark.medium
def test_delete_booking(start_end, get_auth_token, create_booking, get_booking_by_id, delete_booking_by_id):
    create_booking.create_booking()
    booking_id = create_booking.booking_id

    get_auth_token.get_auth_token()

    delete_booking_by_id.delete_booking(booking_id=booking_id, token=get_auth_token.token)
    delete_booking_by_id.check_resp_code_is_201()
