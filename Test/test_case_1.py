from http.client import responses

#st Case 1: Get all rooms
#1. Send GET request to '/rooms'
#2. Verify response status is 200
#3. Verify response body is not empty
#4. Verify list of rooms is returned

import pytest
import requests

def test_cases_1_get_all_rooms():
        response = requests.get(url = "https://automationintesting.online/api/room")
        assert response.status_code == 200
