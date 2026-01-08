class User:
    age = 0
    name = ""
    email = ""

phone_number = "+1.."

num1 = 10
num2 = 20

user1 = User()
user1.age = num1
user1.email = "tester@example.com"
user1.name = "Kostya"
user1.phone_number = "+1.."

user2 = User()
user2.age = num2
user2.email = "john@example.com"
user2.name = "John"

print(user1.age)
user1.age = 45
print(user1.age)
print(user1.phone_number)