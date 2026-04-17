# Test Case 8: Create booking with invalid dates

import requests


def test_Create_booking_with_invalid_dates():
    payload = [ {
        "roomid": 1,
        "lastname": "Junior",
        "firstname": "Boris",
        "totalprice": 100,
        "depositpaid": "True",
        "bookingdates": {
            "checkin": "2026-04-12",
            "checkout": "2026-04-12"
        },
        "additionalneeds": "Breakfast"
    },
     {
        "roomid": 1,
        "lastname": "Junior",
        "firstname": "Boris",
        "totalprice": 100,
        "depositpaid": "True",
        "bookingdates": {
            "checkin": "2026-04-12",
            "checkout": "2026-04-12"
        },
        "additionalneeds": "Breakfast"
    }]

    response = requests.post("https://automationintesting.online/api/booking",
                             json=payload
                             )
    print(response.status_code)
    print(response.text)
    assert response.status_code in [400, 409]
