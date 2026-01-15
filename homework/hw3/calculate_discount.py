def calculate_discount(sum , discount):
    discount_amount = sum - sum * discount/100
    return discount_amount

print(calculate_discount(120,10))
print(calculate_discount(1670,8))