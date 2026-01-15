nums = [10, 34, 25, 67, 8, 55, 11, 3, 42]

def check_num(number):
    if number % 2 == 0:
        print("The number", num, "is even")
    else:
        print("The number", num, "is odd")

def print_if_even(number):
    if number % 2 == 0:
        print("The number", number, "is even")
def print_if_odd(number):
    if number % 2 == 1:
        print("The number", number, "is even")
 
val = input("Enter 'odd' or 'even': ")
if val.startswith("o"):
    for num in nums:
        print_if_odd(num)
elif val.startswith("e"):
    for num in nums:
        print_if_even(num)
else:
    print("The command is undefined ")      
