class User:
    name = ""
    age = 0
    email = ""

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        print(name + " is created")
