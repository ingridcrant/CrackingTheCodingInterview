"""
Write an algorithm such that if an element in an mxn matrix is 0, its entire row 
and column are set to 0.
"""

def settozero(matrix):
    m = len(matrix)
    n = len(matrix[m - 1])

    rows = set()
    cols = set()

    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                rows.add(row)
                cols.add(col)
    
    for row in range(m):
        for col in range(n):
            if row in rows or col in cols:
                matrix[row][col] = 0
    
    return matrix

# test case
matrix = [[1, 0, 0], [2, 3, 4], [5, 6, 7]]
shifted = settozero(matrix)

for row in shifted:
    print(row)