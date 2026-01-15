global_var = 1

def print_global():
    print(global_var)

def print_local():
    local_var = 2
    print(local_var)

def print_param(val1):
    print(val1)

print_local()
# print(local_var)
print_param(777)