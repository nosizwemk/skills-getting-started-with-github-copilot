from urllib.parse import quote


def test_signup_adds_new_participant(client, isolated_activities):
    # Arrange
    activity_name = "Chess Club"
    email = "new.student@mergington.edu"
    activity_path = quote(activity_name, safe="")

    # Act
    response = client.post(f"/activities/{activity_path}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for {activity_name}"}
    assert email in isolated_activities[activity_name]["participants"]


def test_signup_returns_404_for_unknown_activity(client):
    # Arrange
    activity_name = "Unknown Club"
    email = "student@mergington.edu"
    activity_path = quote(activity_name, safe="")

    # Act
    response = client.post(f"/activities/{activity_path}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_signup_returns_400_for_duplicate_participant(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    activity_path = quote(activity_name, safe="")

    # Act
    response = client.post(f"/activities/{activity_path}/signup", params={"email": email})

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Student already signed up for this activity"}
