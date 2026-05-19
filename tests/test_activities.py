def test_get_activities_returns_expected_structure(client):
    # Arrange
    required_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert "Chess Club" in payload

    for details in payload.values():
        assert required_keys.issubset(details.keys())
        assert isinstance(details["participants"], list)


def test_get_activities_contains_seed_participants(client):
    # Arrange
    activity_name = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert "michael@mergington.edu" in payload[activity_name]["participants"]
