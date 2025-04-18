#Write a function that reverses a list without using [::-1] or reverse().
my_list = ['apple','banana','orange','mango']
print(my_list)
new_list = []
for x in range(len(my_list)-1,-1,-1):
    new_list.append(my_list[x])
print(new_list)
