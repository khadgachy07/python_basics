#Return a list of duplicate elements from a given list.
myList = ["apple", "banana", "ball", "mango", "ball", "apple"]
ogList = []
dupliList = []

for item in myList:
    if item in ogList:
        if item not in dupliList:
            dupliList.append(item)
    else:
        ogList.append(item)

print("Original list (unique):", ogList)
print("Duplicate elements:", dupliList)
