#Check if a given string is a palindrome.
my_string = 'madan'
rev_string = []

for x in range(len(my_string) - 1, -1, -1):
    rev_string.append(my_string[x])

# Join list back into a string
reversed_str = ''.join(rev_string)

# Check for palindrome
if my_string == reversed_str:
    print(f"'{my_string}' is a palindrome.")
else:
    print(f"'{my_string}' is not a palindrome.")
