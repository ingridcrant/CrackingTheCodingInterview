"""
Given an image represented by an NxN matrix, where each pixel in the image is
4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""
def swap(matrix, row1, col1, row2, col2):
    temp = matrix[row1][col1]
    matrix[row1][col1] = matrix[row2][col2]
    matrix[row2][col2] = temp

# rotates a matrix clockwise by 90 degrees
def rotateclockwise(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            if j != i:
                swap(matrix, i, j, j, i)
    
    for row in range(n):
        l = 0
        r = n - 1

        while r > l:
            swap(matrix, row, l, row, r)
            l += 1
            r -= 1
    
    return matrix

# test case
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
rotated = rotateclockwise(matrix)

for row in range(len(rotated)):
    print(rotated[row])