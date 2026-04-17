#Test Case 11: Send message with invalid email
#• 1. Send POST request with invalid email
#• 2. Verify response status is 400
#• 3. Verify validation error

import requests
import pytest


class TestRooms:
    def test_cases_10_post_Send_contact_message_with_valid_data(self):
        payload = {
            "name": "boris",
            "email": "gmail.com",
            "phone": "1020304020304",
            "description": "I want to book a room today",
            "subject": "Booking a room"
        }
        response = requests.post(url="https://automationintesting.online/api/message", json=payload)
        assert response.status_code == 400
