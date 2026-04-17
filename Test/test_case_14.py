# Test Case 14: SQL injection attempt

import requests


def test_sql_injection_attempt():
    payload = {
        "roomid": 1,
        "lastname": "' OR 1=1 --",
        "firstname": "Boris",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-04-12",
            "checkout": "2026-04-14"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(
        "https://automationintesting.online/api/booking",
        json=payload
    )

    print(response.status_code)
    print(response.text)

    # 🔥 attendu : rejet
    assert response.status_code in [400, 403]
