import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verification import verfiy_http_status_code, verify_json_key_for_not_null
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Util


class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description(
        "Creating a Booking from the paylaod and verfiy that booking id should not be null and status code should be 200 for the correct payload")
    def test_create_booking_positive(self):
        response = post_request(url=APIConstants.url_create_booking(),
                                auth=None,
                                headers=Util().common_headers_json(),
                                payload=payload_create_booking(),
                                in_json=False)
        
        booking_id = response.json()["bookingid"]
        
        verfiy_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)
    
    @pytest.mark.negative
    def test_create_booking_neagtive(self):
        # URL, Headers, Payload,
        response = post_request(url=APIConstants.url_create_booking(), auth=None, headers=Util().common_headers_json(),
                                 payload={}, in_json=False)
        verfiy_http_status_code(response, 500)
