from lesson_4.player import Player

students = ["Tom", "Bob", "Alex", "Nick", "Kostya", "Mariia", "Tanya"]

# for student in range(0, len(students)):
#     print(student)
#
# for student in range(0, len(students), 2):
#     print(students[student])
#
# for student in range(len(students)-1, -1, -1):
#     print(students[student])
#
# for student in range(-len(students), 0):
#     print(students[student])
#
# for student in range(-1, -len(students), -1):
#     print(students[student])
#
# for student in students:
#     print(student)
players_in_quest = [Player("P1"), Player("P2"), Player("P3"), Player("P4")]
for player in players_in_quest:
    print(player.nickname)

for player in players_in_quest:
    player.upgrade_xp(100)
    print(player.get_info())