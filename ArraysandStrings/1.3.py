"""
Given two strings, write a method to decide if one is a permutation of another
"""

def ifpermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    
    dict1 = {}
    dict2 = {}

    for place in range(len(str1)):
        char1 = str1[place]
        if char1 not in dict1:
            dict1[char1] = 1
        else:
            temp = dict1[char1]
            temp += 1
            dict1[char1] = temp

        char2 = str2[place]
        if char2 not in dict2:
            dict2[char2] = 1
        else:
            temp = dict2[char2]
            temp += 1
            dict2[char2] = temp
    
    if dict1 == dict2:
        return True
    else:
        return False

# test case
str1 = "abcdefghijklmnopqrstuvwxyz02413"
str2 = "abcdefghijklmnopqrstuvwxyz02423"

print(ifpermutation(str1, str2))