import openpyxl
import pytest
from src.utils.utils import Utils
from src.helpers.common_verification import *
from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import post_requests
from src.helpers.payload_manager import payload_create_booking,payload_create_token

@pytest.fixture(scope="session")
def create_token():
    response_token=post_requests(url=APIConstants.url_create_auth(),headers=Utils().common_headers(),auth=None,payload=payload_create_token(),in_json=False)
    verify_http_status_code(response_data=response_token,expected_data=200)
    token=response_token.json()["token"]
    print(token)
    verify_json_key_not_null_token(token)
    verify_response_key_not_none(token)
    return token

@pytest.fixture(scope="session")
def get_booking_id():
    response_create_booking=post_requests(url=APIConstants.url_create_booking(),auth=None,headers=Utils().common_headers(),payload=payload_create_booking(),in_json=False)
    booking_id=response_create_booking.json()["bookingid"]
    print(booking_id)
    verify_http_status_code(response_data=response_create_booking,expected_data=200)
    verify_response_key_not_none(booking_id)
    verify_json_key_not_null(booking_id)
    return booking_id

def read_credentials_from_excel(file_path):
    credentials=[]
    workbook=openpyxl.load_workbook(filename=file_path)
    sheet=workbook.active
    for row in sheet.iter_rows(min_row=2,values_only=True):
        username,password=row
        credentials.append(({
            "username":username,
            "password":password
        }))
    return credentials