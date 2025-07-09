import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking
from src.helpers.api_request_wrapper import post_requests
from src.helpers.common_verification import verify_http_status_code,verify_json_key_not_null
from src.utils.utils import Utils

class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID should not be Null")
    @allure.description("Create a Booking from the payload and verify that Booking ID should not be Null and status code should be 200 for the correct payload")
    def test_create_booking_positive(self):
        response=post_requests(url=APIConstants.url_create_booking(),payload=payload_create_booking(),headers=Utils().common_headers(),auth=None,in_json=False)
        booking_id=response.json()["bookingid"]
        verify_http_status_code(response_data=response,expected_data=200)
        verify_json_key_not_null(booking_id)
    def test_create_booking_negative(self):
        response=post_requests(url=APIConstants.url_create_booking(),payload={},auth=None,headers=Utils().common_headers(),in_json=False)
        verify_http_status_code(response_data=response,expected_data=500)

