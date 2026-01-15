total_score = 0

def update_score(score):
    global total_score
    total_score += score

update_score(12)
update_score(18)
update_score(60)

print(total_score)