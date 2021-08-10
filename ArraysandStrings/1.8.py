"""
Assume you have a method isSubstring which checks if one word is a 
substring of another. Given two strings, s1 and s2, write code to check if s2 is 
a rotation of s1 using one call to isSubstring (e.g., "waterbottle" is a ratation of "erbottlewat")
"""

def isRotation(s1, s2):
    if len(s1) == len(s2) and s1 in (s2 + s2):
        return True
    else:
        return False

# test case
s1 = "waterbottle"
s2 = "erbottlewat"
print(isRotation(s1, s2))