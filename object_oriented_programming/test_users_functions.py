import csv

import pytest


@pytest.fixture
def users():
    with open("users.csv") as csvfile:
        users = list(csv.DictReader(csvfile, delimiter=";"))
    return users

@pytest.fixture
def workers(users):
    workers = [user for user in users if user["status"] == "worker"]
    return workers

def test_workers_are_adults (workers):
    for worker in workers:
        assert user_is_adult(worker), f"Worker age of {worker["name"]} is lower than 18"

def user_is_adult(user):
    return int(user["age"]) >= 18