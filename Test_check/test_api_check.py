import requests
import pytest

def test_get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200


def test_get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    data = response.json()
    print(data)

    assert response.status_code == 200
    assert isinstance(data, list)
    assert data[0]["name"] == "Leanne Graham"


def test_create_user():
    url = "https://jsonplaceholder.typicode.com/users"

    payload = {
        "name": "John",
        "email": "john@test.com"
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 201
    assert response.json()["name"] == "John"


def test_with_headers(): # ce test ne peut pas fonctionner
    url = "https://api.example.com/data"

    headers = {
        "Authorization": "Bearer token123"
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 200




BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0
    assert "title" in data[0]





def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "title" in data


def test_create_post():
    payload = {
        "title": "Test API",
        "body": "Ceci est un test",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Test API"


def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")

    assert response.status_code == 200



@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

def test_example(base_url):
    response = requests.get(f"{base_url}/posts")
    assert response.status_code == 200

from jsonschema import validate

def test_user_schema_advanced():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "email": {"type": "string"},
            "username": {"type": "string"}
        },
        "required": ["id", "email", "username"]
    }

    validate(instance=data[0], schema=schema)



@pytest.mark.parametrize("number, expected", [
    (1, 2),
    (2, 4),
    (3, 6)
])
def test_double(number, expected):
    assert number * 2 == expected




BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.parametrize("user_id", [1, 2, 3, 4])
def test_get_user(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == user_id


@pytest.mark.parametrize("user_id, expected_status", [
    (1, 200),
    (2, 200),
    (999, 404)  # user inexistant
])
def test_user_status(user_id, expected_status):
    response = requests.get(f"{BASE_URL}/users/{user_id}")

    assert response.status_code == expected_status


@pytest.mark.parametrize("payload, expected_title", [
    ({"title": "A", "body": "test", "userId": 1}, "A"),
    ({"title": "B", "body": "test", "userId": 1}, "B"),
])
def test_create_post(payload, expected_title):
    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == expected_title