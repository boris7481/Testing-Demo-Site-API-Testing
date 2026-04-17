#Twsst Case 4: Get valid room by ID
#1. Send GET request to '/room/1'
#2. Verify response status is 200
#3. Verify correct room data is returned



import requests
import pytest

class TestRooms:
    def test_cases_4_get_valid_room_by_ID(self):
        response = requests.get(url ="https://automationintesting.online/api/room/1/")
        assert response.status_code == 200