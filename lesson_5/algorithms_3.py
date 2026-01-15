import random

from lesson_3.player import Player

players = []
list_to_invite = []
loosers_list = []

def number_of_players_in_two_lists(list1, list2):
     return len(list1) + len(list2)

for i in range(0, 100):
     players.append(Player("P"+ str(i+1)))
     players[i].upgrade_xp(random.randint(500, 1500 ))

print("The players list is:")
for player in players:
     print(player.get_info())

for player in players:
     if player.xp >= 1000:
          list_to_invite.append(player)
     else:
          loosers_list.append(player)

print("The players list include:")
for player in list_to_invite:
     print(player.get_info())
print("Number of participating players is:", len(list_to_invite))
print("==========================================================================")

print("The loosers list includes: ")
for player in loosers_list:
     print(player.get_info())
print("Number of non-participating players is:", len(loosers_list))
print("==========================================================================")

print("Number of participating and non-participating players in current game is:", number_of_players_in_two_lists(list_to_invite, loosers_list))