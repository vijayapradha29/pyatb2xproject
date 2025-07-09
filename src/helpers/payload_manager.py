from faker import Faker

def payload_create_booking():
    payload={
        "firstname": "Jim",
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
    faker=Faker()
    payload={
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(100,1000),
        "depositpaid": faker.boolean(),
        "bookingdates": {
            "checkin": faker.date_between_dates("2019-01-01","2025-07-08"),
            "checkout": faker.date_between_dates("2019-01-01","2025-07-08")
        },
        "additionalneeds": faker.random_element(elements=("Breakfast","Lunch","Dinner"))
    }
    return payload

def payload_create_token():
    payload={
        "username": "admin",
        "password": "password123"
    }
    return payload