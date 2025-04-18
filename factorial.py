#Write a recursive function to find factorial of a number.
def factorialNum(myNum):
    factorial = 0
    if myNum == 0 or myNum == 1:
        factorial = 1
    else:
        factorial = myNum * factorialNum(myNum-1)
    return factorial
print(factorialNum(5))
