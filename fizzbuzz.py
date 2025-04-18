#Print numbers from 1 to 100. For multiples of 3 print “Fizz”, for 5 “Buzz”, for both “FizzBuzz”.
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print(x, ": FizzBuzz")
    elif x % 5 == 0:
        print(x, ": Buzz")
    elif x % 3 == 0:
        print(x, ": Fizz")
    else:
        print(x)
