"""
Implement a method to perform basic string compression using the counts 
of repeated characters. For example, the string aabcccccaaa would become 
a2b1c5a3. If the "compressed" string would not become smaller than the original 
string, your method should return the original string. You can assume the string 
has only upper and lower case letters (a - z).
"""

def compressstring(string):
    if len(string) == 0:
        return string
    
    char_count = 0
    current_char = string[0]
    compressed_string = ""

    for char in string:
        if char == current_char:
            char_count += 1
        else:
            compressed_string += current_char + str(char_count)
            char_count = 1
            current_char = char
    
    compressed_string += current_char + str(char_count)

    if len(compressed_string) < len(string):
        return compressed_string
    else:
        return string

# test case
print(compressstring("aabcccccaaa"))