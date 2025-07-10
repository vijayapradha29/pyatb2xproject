'''
1.Read the CSV or Excel file
2.Create a function create_token which can take the values from the excel or csv file
3.verify the expected result
'''

import openpyxl
import pytest
import requests

from conftest import read_credentials_from_excel
from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import post_requests
from src.helpers.payload_manager import payload_create_token
from src.utils.utils import Utils
from src.helpers.common_verification import *


# def read_credentials_from_excel(file_path):
#     credentials=[]
#     workbook=openpyxl.load_workbook(filename=file_path)
#     sheet=workbook.active
#     for row in sheet.iter_rows(min_row=2,values_only=True):
#         username,password=row
#         credentials.append(({
#             "username":username,
#             "password":password
#         }))
#     return credentials

def create_token(username,password):
    payload={
        "username":username,
        "password":password
    }
    response_create_token=post_requests(url=APIConstants.url_create_auth(),auth=None,headers=Utils().common_headers(),payload=payload,in_json=False)
    return response_create_token

@pytest.mark.parametrize("user_cred",read_credentials_from_excel("C:\\Users\\Dhivya\\pyatb2xproject\\tests\\test\\data_driven_testing\\MOCK_DATA.xlsx"))
def test_create_auth_with_excel(user_cred):
    username=user_cred["username"]
    password=user_cred["password"]
    print(username,password)
    response=create_token(username=username,password=password)
    print(response.status_code)