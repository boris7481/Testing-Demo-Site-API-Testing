#Test Case 2: Verify room structure
#• 1. Send GET request to '/rooms'
#• 2. Verify response status is 200
#• 3. Verify each room contains fields (id, name, description, price)

import requests
import pytest

import requests
import pytest


class TestRooms:
    def test_cases_2_get_verify_room_structure(self):
        response = requests.get("https://automationintesting.online/api/room")

        assert response.status_code == 200

        data = response.json()

        # ✅ Vérifier que c'est un dictionnaire
        assert isinstance(data, dict)

        # ✅ Vérifier clé 'rooms'
        assert "rooms" in data

        rooms = data["rooms"]

        # ✅ Vérifier que rooms est une liste
        assert isinstance(rooms, list)

        # ✅ Vérifier chaque room
        for room in rooms:
            assert "roomid" in room
            assert "roomName" in room
            assert "description" in room
            assert "roomPrice" in room