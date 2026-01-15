from player import Player

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"]
length: int = len(weekdays)
print(length)
print("Today is", weekdays[5])

numbers = [49, -3, 87, 2]
print(numbers)
print(len(numbers))

p1 = Player("Tom Hardy")
p2 = Player("Tom Holland")
p3 = Player("Tom Cruz")

players = [p1, p2, p3]
print(len(players))
print(players[1].nickname)
print(players[1].get_info())
players[1].upgrade_xp(23)
print(players[1].get_info())

fruits = ['🍌', '🍒', '🍐', '🍈', '🍇', '🍊', '🍉', '🍓', '🍍', '🍎', '🍏', '🍑', '🥝', '🥥', '🥭']
print(fruits)

