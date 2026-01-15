s = 0
nums = [10, 34, 25, 67, 8, 55, 11, 3, 42]

for num in nums:
    s+=num
print(s)

p = 1
for num in nums:
    p*=num
print(p)

string = ""
for i in range(1, 10):
    string += str(i)
print(string)  
