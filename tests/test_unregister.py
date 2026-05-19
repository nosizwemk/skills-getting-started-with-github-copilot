from urllib.parse import quote


def test_unregister_removes_existing_participant(client, isolated_activities):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    activity_path = quote(activity_name, safe="")

    # Act
    response = client.post(f"/activities/{activity_path}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity_name}"}
    assert email not in isolated_activities[activity_name]["participants"]


def test_unregister_returns_404_for_unknown_activity(client):
    # Arrange
    activity_name = "Unknown Club"
    email = "student@mergington.edu"
    activity_path = quote(activity_name, safe="")

    # Act
    response = client.post(f"/activities/{activity_path}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_returns_404_for_non_participant(client):
    # Arrange
    activity_name = "Chess Club"
    email = "not.enrolled@mergington.edu"
    activity_path = quote(activity_name, safe="")

    # Act
    response = client.post(f"/activities/{activity_path}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Student not signed up for this activity"}
