num = int(in5put("enter the number:"))
fact = 1
if num < 0:
    print("sorry, factorial doe not exist for negative number ")
elif num == 0:
    print("the factorial for 0 is 1")
else:
    for i in range(1, num + 1):
        fact = fact * i
    print("the factorial of", num, "is", fact)
