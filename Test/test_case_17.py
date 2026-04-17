# est Case 17: Unsupported HTTP method
# 1. Send PUT request to '/rooms'
# 2. Verify response status is 405


import pytest
import requests


class TestRooms:
    def test_cases_13_invalid_endpoint(self):
        response = requests.put(url="https://automationintesting.online/api/rooms")
        assert response.status_code in [404, 405]
