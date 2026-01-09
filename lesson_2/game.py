from classes.character import Character

char1 = Character("Boba Fet", "male")
char1.balance = 2
char1.gender = "male"
char1.health = 100
char1.xp = 20
char1.is_verified = True
char1.name = "Boba Fet"

print(char1.name, char1.gender, char1.xp, char1.balance)
