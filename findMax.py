#Write a function to return the maximum number from a list without using max().
my_list = [2,5,6,7,99,80,55,100]
high_num = 0
for x in range(0,len(my_list),1):
    if high_num < my_list[x]:
        high_num = my_list[x]
print(high_num,"high")
