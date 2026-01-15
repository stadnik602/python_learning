from lesson_4.player import Player

def print_number(number):
    for i in range(1,  number):
        player = Player("Player " + str(i))
        player.upgrade_xp(i)
        print(player.get_info())
print_number(10)

s = 0
for number in range(1, 6):
    s += number
print(s)

for x in range(0, 101, 5):
    print(x)

for i in range(1, 6):
    print("*" * i)