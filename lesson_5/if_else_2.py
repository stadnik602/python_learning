num = 12

def is_odd(number):
    return number % 2

if is_odd(num):
    print("The number is odd,", num)
else:
    print("The number is even,", num)

def get_val():
    # return [1, 2, 4] #true
    return [] #false

if get_val():
    print("Yes")
else:
    print("No")