class Character:
    health = 0
    name = ""
    xp = 0
    balance = 0
    is_verified = False
    gender = "" #"male" "female"

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
