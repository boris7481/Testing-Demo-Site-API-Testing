# Test Case 7: Create booking with missing fields

import requests

# the test is wright and ppassed with Postman
def test_Create_booking_with_missing_fields():
    payload = {
        "roomid": 1,
        "lastname": "Junior",
        "totalprice": 100,
        "depositpaid": "True",
        "bookingdates": {
            "checkin": "2026-04-10",
            "checkout": "2026-04-12"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post("https://automationintesting.online/api/booking",
                            json=payload)

    print(response.status_code)
    print(response.text)
    print(response.json())
    assert response.status_code == 400
