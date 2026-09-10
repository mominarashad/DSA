class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        m = len(matrix[0])   # columns
        n = len(matrix)      # rows

        first_row = False
        first_col = False

        # Mark rows and columns that need to become zero
        for i in range(n):
            for j in range(m):

                if matrix[i][j] == 0:

                    if i == 0:
                        first_row = True

                    if j == 0:
                        first_col = True

                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Set cells to zero based on markers
        for i in range(1, n):
            for j in range(1, m):

                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # Handle first row
        if first_row:
            for j in range(m):
                matrix[0][j] = 0

        # Handle first column
        if first_col:
            for i in range(n):
                matrix[i][0] = 0