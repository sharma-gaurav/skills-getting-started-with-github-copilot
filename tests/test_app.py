from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_signup_success():
    # Arrange
    email = "newstudent@mergington.edu"
    activity = "Chess Club"
    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})
    # Assert
    assert response.status_code == 200
    assert f"Signed up {email}" in response.json()["message"]

def test_signup_duplicate():
    # Arrange
    email = "newstudent@mergington.edu"
    activity = "Chess Club"
    client.post(f"/activities/{activity}/signup", params={"email": email})
    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})
    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]

def test_unregister_success():
    # Arrange
    email = "newstudent@mergington.edu"
    activity = "Chess Club"
    client.post(f"/activities/{activity}/signup", params={"email": email})
    # Act
    response = client.post(f"/activities/{activity}/unregister", params={"email": email})
    # Assert
    assert response.status_code == 200
    assert f"Unregistered {email}" in response.json()["message"]

def test_unregister_not_signed_up():
    # Arrange
    email = "ghost@mergington.edu"
    activity = "Chess Club"
    # Act
    response = client.post(f"/activities/{activity}/unregister", params={"email": email})
    # Assert
    assert response.status_code == 400
    assert "not signed up" in response.json()["detail"]
