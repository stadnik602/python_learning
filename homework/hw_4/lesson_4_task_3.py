import random

list = ["Python", "C#", "JavaScript", "Ruby"]
list.append("Java")
list.remove(list[random.randint(0, len(list) - 1)])
print(list)
