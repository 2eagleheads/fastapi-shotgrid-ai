import pytest
from syrupy.assertion import SnapshotAssertion
from tests.conftest import client

def test_get_projects(snapshot: SnapshotAssertion):
    response = client.get("/projects/")
    assert response.status_code == 200
    assert snapshot == response.json()

def test_create_project(snapshot: SnapshotAssertion):
    project_data = {"name": "Test Project", "code": "TP", "description": "Test Description"}
    response = client.post("/projects/", json=project_data)
    assert response.status_code == 200
    assert snapshot == response.json()