'''
1.create token
2.create booking
3.update the booking(PUT)
4.Delete the booking

For updating the booking we need token and booking id
and then we need to send or transfer that datas to update booking
the sharing of data can be done by using fixture in pytest
'''

import pytest
import allure
from faker.proxy import Faker

from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.helpers.api_request_wrapper import *
from src.helpers.common_verification import verify_http_status_code, verify_json_key_not_null, \
    verify_response_key_not_none, verify_json_key_not_null_token, verify_response_text, verify_response_text_type, \
    verify_response_key
from src.utils.utils import Utils

class TestCrud():
    #def get_booking_id and def create_token->both are normal functions
    # @pytest.fixture()
    # def create_token(self):
    #     response_token=post_requests(url=APIConstants.url_create_auth(),headers=Utils().common_headers(),auth=None,payload=payload_create_token(),in_json=False)
    #     verify_http_status_code(response_data=response_token,expected_data=200)
    #     token=response_token.json()["token"]
    #     print(token)
    #     verify_json_key_not_null_token(token)
    #     verify_response_key_not_none(token)
    #     return token
    #
    # @pytest.fixture()
    # def get_booking_id(self):
    #     response_create_booking=post_requests(url=APIConstants.url_create_booking(),auth=None,headers=Utils().common_headers(),payload=payload_create_booking(),in_json=False)
    #     booking_id=response_create_booking.json()["bookingid"]
    #     print(booking_id)
    #     verify_http_status_code(response_data=response_create_booking,expected_data=200)
    #     verify_response_key_not_none(booking_id)
    #     verify_json_key_not_null(booking_id)
    #     return booking_id

    @allure.title("Test CRUD Operation Update(PUT")
    @allure.description("Verify that Full Update with Booking ID and Token is Working")
    def test_update_booking_with_token_and_booking_id(self,create_token,get_booking_id):
        response_update=put_requests(url=APIConstants.url_put_patch_delete(booking_id=get_booking_id),auth=None,headers=Utils().common_header_put_patch_delete_with_token(token=create_token),payload=payload_create_booking(),in_json=False)
        print(response_update.json())
        verify_http_status_code(response_data=response_update,expected_data=200)
        first_name=response_update.json()["firstname"]
        verify_json_key_not_null_token(first_name)
        verify_response_key(key=first_name,expected_data="Jim")
        verify_response_key(key=response_update.json()["lastname"],expected_data="Brown")



    @allure.title("Test CRUD Operation Delete")
    @allure.description("Verify that Deleting Booking with Token and Booking ID is Working")
    def test_delete_booking_with_token_and_booking_id(self,create_token,get_booking_id):
        response_delete=delete_requests(url=APIConstants.url_put_patch_delete(booking_id=get_booking_id),auth=None,headers=Utils().common_header_put_patch_delete_with_token(token=create_token),in_json=False)
        print(response_delete.status_code)
        verify_http_status_code(response_data=response_delete,expected_data=201)
        responseText=response_delete.text
        print(responseText)
        # verify_response_text(responseText)
        # assert responseText=="Created"
        verify_response_text_type(responseText)
        verify_response_text(response_data=responseText,expected_text="Created")