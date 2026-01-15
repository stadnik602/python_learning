from time import perf_counter
start = perf_counter()
for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
finish = perf_counter()

start2 = perf_counter()
for i in range(1,101):
    result = ""
    if i % 3 == 0:
        result += "Fizz"
    if i % 5 == 0:
        result += "Buzz"
    if i % 3 != 0 and i % 5 != 0:
        result += str(i)
    print(result)
finish2 = perf_counter()

print(finish - start)
print(finish2 - start2)