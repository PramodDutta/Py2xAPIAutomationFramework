# payloads
# dict ->
from faker import Faker
import json

faker = Faker()

def payload_create_booking():
    payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_create_booking_dynamic():
    payload = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=1000),
        "depositpaid": faker.boolean(),
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": faker.random_element(elements=("Breakfast", "Parking", "WiFi", "Extra Bed"))
    }
    return payload

def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload



# def payload_create_booking_data_excel():
#     payload = {
#         "firstname": read_From_excel["fistname"],
#         "lastname": faker.last_name(),
#         "totalprice": faker.random_int(min=100, max=1000),
#         "depositpaid": faker.boolean(),
#         "bookingdates": {
#             "checkin": "2018-01-01",
#             "checkout": "2019-01-01"
#         },
#         "additionalneeds": faker.random_element(elements=("Breakfast", "Parking", "WiFi", "Extra Bed"))
#     }
#     return payload
