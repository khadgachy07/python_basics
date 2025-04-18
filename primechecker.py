my_num = 6

if my_num <= 1:
    print("not prime")
elif my_num == 2:
    print("prime")
elif my_num % 2 == 0:
    print("not prime")
else:
    for x in range(3, int(my_num**0.5) + 1, 2):
        if my_num % x == 0:
            print("not prime")
            break
    else:
        print("prime")
