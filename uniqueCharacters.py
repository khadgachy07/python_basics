#Check if a string has all unique characters.
def has_unique(myStr):
    myStr = myStr.lower()
    seen = set()
    for char in myStr:
        if char in seen:
            return False
        seen.add(char)
    return True

print(has_unique('abecda'))
