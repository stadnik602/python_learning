import csv

from models.users import User, Status


class UserProvider:
    def get_users(self) -> list[User]:
        raise NotImplementedError()

class CsvUserProvider(UserProvider):
    def get_users(self) -> list[User]:
        with open("users.csv") as csvfile:
            users = csv.DictReader(csvfile, delimiter=';')
            return [
                User(name=user["name"],
                     age=int(user["age"]),
                     status=Status(user["status"]),
                     items=user["items"]
                     )
                for user in users
            ]


class DatabaseUserProvider(UserProvider):
    def get_users(self) -> list[User]:
        raise NotImplementedError()

class APIUserProvider(UserProvider):
    def get_users(self) -> list[User]:
        raise NotImplementedError()