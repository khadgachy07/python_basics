#Write a function to return first n Fibonacci numbers.
def getFibonacciNum(n):
    fib_seq = []
    a,b = 0,1
    for x in range(n):
        fib_seq.append(a)
        a,b = b, a+b
    return fib_seq

print(getFibonacciNum(5))
