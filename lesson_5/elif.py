status = "fail"

if status == "ok":
    print("The payment is accepted")
elif status == "wait":
    print("waiting of payment")
elif status == "fail":
    print("The payment is rejected")
else:
    print("Unknown status")