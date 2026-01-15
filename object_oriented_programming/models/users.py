from dataclasses import dataclass
from enum import Enum

USER_ADULT_AGE = 18

class Status(Enum):
    student = "student"
    worker = "worker"

@dataclass
class User:
    name: str
    age: int
    status: Status
    items: list[str]

    def is_adult(self):
        return self.age >= USER_ADULT_AGE

class Worker(User):
    status: Status.worker

    def __init__(self, name: str, age: int, items: list[str]):
        self.name = name
        self.age = age
        self.items = items

    # def __init__(self, name: str, age: int, status: str, items: list[str]):
    #     self.name = name
    #     self.age = age
    #     self.status = status
    #     self.items = items

    # def __eq__(self, other):
    #     return (self.name == other.name and
    #             self.age == other.age and
    #             self.status == other.status and
    #              self.items == other.items)

if __name__ == "__main__":
    d = {"name": "Oleg",
         "age": 16,
         "status": "student",
         "items": ["book", "pen", "paper"]}

oleg = User(name="Oleg", age=16, status=Status.student, items=["book", "pen", "paper"])
oleg2 = User(name="Oleg", age=16, status=Status.student, items=["book", "pen", "paper"])
anna = User(name="Anna", age=18, status=Status.worker, items=["pen", "eraser", "notebook"])

olga_worker = Worker(name="Olga", age=20, items=["pen", "eraser", "notebook"])

assert oleg == oleg2
assert oleg.age == 16
assert anna.age == 18

anna.age += 1
assert anna.age == 19