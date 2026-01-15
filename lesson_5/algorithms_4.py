import random
from time import perf_counter

from lesson_5.player import Player

participants = []
s = [] # 70 - 79 -> Small
m = [] # 80 - 99 -> Medium
l = [] # 100 - 119 -> Large
xl = [] # 120+ -> Extra Large

s2 = [] # 70 - 79 -> Small
m2 = [] # 80 - 99 -> Medium
l2 = [] # 100 - 119 -> Large
xl2 = [] # 120+ -> Extra Large

def fill_participants_list(number_of_participants):
    for x in range(0, number_of_participants):
        weight = random.randint(60, 130)
        participants.append(Player(f"Player {x+1}", weight))

def sort_in_lists_by_category(participants_list):
    for participant in participants_list:
        if participant.weight < 80:
            s.append(participant)
        elif 80 <= participant.weight <= 99:
            m.append(participant)
        elif 100 <= participant.weight < 120:
            l.append(participant)
        else:
            xl.append(participant)
def sort_in_lists_by_category_new(participants_list):
    for participant in participants_list:
        if participant.weight < 100:
            if participant.weight >= 80:
                m2.append(participant)
            else:
                s2.append(participant)
        elif participant.weight < 120:
            l2.append(participant)
        else:
            xl2.append(participant)

def print_participants_info(participants):
    for participant in participants:
        print(participant.get_info())

def set_participants_category(participants_list):
    for participant in participants_list:
        if participant.weight < 80:
            participant.update_category("Small")
        elif 80 <= participant.weight <= 99:
            participant.update_category("Medium")
        elif 100 <= participant.weight < 120:
            participant.update_category("Large")
        else:
            participant.update_category("Extra Large")

def print_participants_in_selected_category():
    user_category = input("Please enter your category: ")
    if user_category.capitalize().startswith('S'):
        print_participants_info(s)
    elif user_category.capitalize().startswith('M'):
        print_participants_info(m)
    elif user_category.capitalize().startswith('L'):
        print_participants_info(l)
    elif user_category.capitalize().startswith('E'):
        print_participants_info(xl)
    else:
        print("You entered invalid category.")

fill_participants_list(100)
set_participants_category(participants)

start = perf_counter()
sort_in_lists_by_category(participants)
finish = perf_counter()
print(("old result:", str(finish - start)))

start = perf_counter()
sort_in_lists_by_category_new(participants)
finish = perf_counter()
print(("new result:", str(finish - start)))
print_participants_info(participants)
# print_participants_in_selected_category()

