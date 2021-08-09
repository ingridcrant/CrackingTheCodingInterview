import time

"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""

# brute force algorithm for checking if a string has all unique characters - O(n^2)
def bruteforce(string):
    start = time.time()

    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i] == string[j]:
                end = time.time()
                print("time elapsed:", end - start)
                return False
    
    end = time.time()
    print("time elapsed:", end - start)
    return True

# efficient algorithm for checking if a string has all unique characters - O(n)
def moreefficient(string):
    start = time.time()

    characters = [False] * 256
    for char in string:
        if not characters[ord(char)]:
            characters[ord(char)] = True
        else:
            return False
    
    end = time.time()
    print("time elapsed:", end - start)
    return True

# another efficient algorithm for checking if a string has all unique characters using sets() - O(n)
def anotherefficient(string):
    start = time.time()
    char_set = set(string)

    if len(char_set) == len(string):
        end = time.time()
        print("time elapsed:", end - start)
        return True
    else:
        end = time.time()
        print("time elapsed:", end - start)
        return False

# test case
test_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

print("brute force")
print(bruteforce(test_string))

print("efficient using boolean list")
print(moreefficient(test_string))

print("efficient using hashset")
print(anotherefficient(test_string))