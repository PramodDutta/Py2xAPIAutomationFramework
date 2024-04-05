# Read the CSV or EXCEL file
# Create a Function create_token which can take values from the Excel File
# Verify the Expected Result.

# Read the Excel - openpyxl
import openpyxl
import requests

from src.constants.api_constants import APIConstants
from src.utils.utils import Util
from src.helpers.api_requests_wrapper import *


def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(filename=file_path)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username,password = row
        credentials.append(({
            "username" : username,
            "password" : password
        }))
    return credentials
    


def create_auth_request(username,password):
    payload = {
        "username": username,
        "password": password
    }
    response = post_request(
        url=APIConstants.url_create_token(),
        headers=Util().common_headers_json(),
        auth=None,
        payload=payload,
        in_json=False
    )
    return response
    


def test_create_auth_with_excel():
    file_path = "/Users/pramod/PycharmProjects/Py2xAPIAutomationFramework/tests/test/datadriventesting/testdata_ddt_123.xlsx"
    credentials = read_credentials_from_excel(file_path=file_path)
    print(credentials)
    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username,password)
        response = create_auth_request(username=username,password=password)
        print(response.status_code)


