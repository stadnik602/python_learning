x = 1
def funcA():
    y = 2
    print("Started to do A")
    funcB()
    print("Finished to do A")

def funcB():
    print("Started to do B")
    funcC()
    print("Finished to do B")

def funcC():
    print("Started to do C")
    funcD()
    print("Finished to do C")

def funcD():
    print("Finished to do D")

print("Started the program")
funcA()
print("Finished the program")