#Given a string, return a dictionary of word counts.
myStr = "Hello, World! Hello, World!"
lowStr=myStr.lower()
words = lowStr.split()

count_dst = {}

for word in words:
    if word in count_dst:
        count_dst[word] += 1
    else:
        count_dst[word] = 1
print(count_dst)
