# Test Case 10: Send contact message with valid data
# • 1. Send POST request to '/message'
# • 2. Provide valid name, email, phone, message
# • 3. Verify response status is 200
# • 4. Verify success message


import requests
import pytest


class TestRooms:
    def test_cases_10_post_Send_contact_message_with_valid_data(self):
        payload = {
            "name": "boris",
            "email": "test@gmail.com",
            "phone": "1020304020304",
            "description": "I want to book a room today",
            "subject": "Booking a room"
        }
        response = requests.post(url="https://automationintesting.online/api/message", json=payload)
        assert response.status_code == 200
