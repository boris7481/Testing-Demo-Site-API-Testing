#Test Case 5: Get invalid room ID
#• 1. Send GET request to '/room/9999'
#• 2. Verify response status is 404
#• 3. Verify error message is returned



import requests
import pytest

class TestRooms:
    def test_cases_5_get_invalid_room_by_id(self):
        response = requests.get(url ="https://automationintesting.online/api/room/9999/")
        assert response.status_code == 500