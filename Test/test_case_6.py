import requests
import pytest
json_response = {
            "roomid": 1,
            "roomName": "101",
            "type": "Single",
            "accessible": "true",
            "image": "/images/room1.jpg",
            "description": "Aenean porttitor mauris sit amet lacinia molestie. In posuere accumsan aliquet. Maecenas sit amet nisl massa. Interdum et malesuada fames ac ante.",
            "features": [
                "TV",
                "WiFi",
                "Safe"
            ],
            "roomPrice": 100
        }

import requests

def test_create_booking_valid_data():
    payload = {
        "roomid": 1,
        "firstname": "Boris",
        "lastname": "Junior",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-04-10",
            "checkout": "2026-04-12"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(
        "https://automationintesting.online/api/booking",
        json=payload
                    )

    print(response.status_code)
    print(response.text)

    assert response.status_code in [200, 201]