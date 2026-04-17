# AUTH / EDGE CASES
# Test Case 16: Large payload handling
import requests

def test_Large_payload_handling():
    payload ={
        "roomid": 1,
        "lastname": "boris",
        "firstname": "Boris",
        "totalprice": 100,
        "depositpaid": "True",
        "bookingdates": {
            "checkin": "2026-04-12",
            "checkout": "2026-04-14"
        },
        "additionalneeds": "Breakfast dddddddddddddddddddddddddddddddddddddddddddddddddddddrrrrg"
                           "ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
                           "gggggggggggggggggggggggggggggggggggggggggggggkjiihuhubhbuguhbbubjbjnnieh"
                           "ihufekoooaoaoaoaooddkdkdkdkdjfjfjfjfjfjfjfjnmmfmmfkdkdkdkdkdkkdkdkdd"
                           "kdkdkdkdkdkdkdkdkdkdkd"
    }

    response = requests.post(
        "https://automationintesting.online/api/booking",
        json=payload
    )

    print(response.status_code)
    print(response.text)


    assert response.status_code == 401
# different result in postman --> to be check