import csv

import pytest
from models.users import User, Status, Worker
from models.providers import UserProvider, CsvUserProvider
from models.users import USER_ADULT_AGE
from models.providers import DatabaseUserProvider, APIUserProvider


@pytest.fixture(params=[CsvUserProvider, DatabaseUserProvider, APIUserProvider])
def user_provider(request) -> UserProvider:
    return request.param()

@pytest.fixture
def users(user_provider) -> list[User]:
    return user_provider.get_users()

@pytest.fixture
def workers(users) -> list[Worker]:
    workers = [Worker(name=user.name, age=user.age, items=user.items)
               for user in users if user.status == Status.worker]
    return workers

def test_workers_are_adults (workers):
    for worker in workers:
        assert worker.is_adult, f"Worker age of {worker.name} is lower than {USER_ADULT_AGE}"

if __name__ == "__main__":
    d = {"name": "Oleg",
         "age": 16,
         "status": "student",
         "items": ["book", "pen", "paper"]}
