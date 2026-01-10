from player import Player

player1 = Player("Minorium")
print(player1.xp)

player1.upgrade_xp(15)
print(player1.xp)

player1.upgrade_xp(22 )
print(player1.xp)

print(player1.get_info())
