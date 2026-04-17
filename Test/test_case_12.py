#Test Case 12: Send message with empty fields
#• 1. Send POST request with empty payload
#• 2. Verify response status is 400
#• 3. Verify required field errors


import requests
import pytest


class TestRooms:
    def test_cases_10_post_Send_contact_message_with_valid_data(self):
        payload = {
          
        }
        response = requests.post(url="https://automationintesting.online/api/message", json=payload)
        assert response.status_code == 400