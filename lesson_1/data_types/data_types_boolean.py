on = True
off = False

print(on)
print(off)

#NOT
print(not on)
print(not off) #True

#AND
user_login_is_valid = True
password_is_correct = False
is_auth = user_login_is_valid and password_is_correct
print(is_auth) #False

#OR
promo_code_used = False
paid_by_card = True
is_paid = promo_code_used or paid_by_card
print(is_paid) #True
promo_code_used = False
paid_by_card = False
is_paid_false = promo_code_used or paid_by_card
print(is_paid_false) #False

#EQUALS
are_equals = on == off
print(are_equals)