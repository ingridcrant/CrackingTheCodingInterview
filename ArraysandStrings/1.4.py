"""
Write a method to replace all spaces in a string with '%20'. You may assume that
the string has sufficient space at the end of the string to hold the additional 
characters, and that you are given the "true" length of the string. (Note: if implementing
in Java, please use a character array so that you can perform this operations in place.)
"""

def replacespaces(string):
    replacement = "%20"
    oglen = len(string)
    current_place = 0
    lenreplacement = len(replacement)
    iter_count = 0

    while iter_count < oglen:
        if string[current_place] == " ":
            string = string[:current_place] + replacement + string[(current_place+1):]
            current_place += lenreplacement - 1
        else:
            current_place += 1
        iter_count += 1
    
    return string

# test case
string = "This is a test"
print(replacespaces(string))
    