import requests
import json

def test_XSS_injection_attempt():
    payload = {
            "roomid": 1,
            "lastname": "Junior",
            "firstname": "<script>alert(1)</script>",
            "totalprice": 100,
            "depositpaid": "True",
            "bookingdates": {
                "checkin": "2026-04-12",
                "checkout": "2026-04-14"
            },
            "additionalneeds": "Breakfast"
        }
    response = requests.post("http://127.0.0.1:5000/xss/", json=payload)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 400
