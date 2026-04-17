#Test Case 13: Invalid endpoint
#• 1. Send GET request to '/invalid-endpoint'
#• 2. Verify response status is 404



import pytest
import requests


class TestRooms:
    def test_cases_13_invalid_endpoint(self):
        response = requests.get(url = "https://automationintesting.online/a")
        assert response.status_code == 404