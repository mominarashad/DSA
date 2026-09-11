class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        first_row=False
        first_col=False

        m=len(matrix[0])
        n=len(matrix)

        for i in range(n):
            for j in range(m):

                if matrix[i][j]==0:

                    if i==0:
                        first_row=True
                    if j==0:
                        first_col=True

                    matrix[0][j]=0
                    matrix[i][0]=0

        for i in range(1,n):
            for j in range(1,m):

                if matrix[i][0]==0 or matrix[0][j]==0:
                      matrix[i][j]=0

        
        if first_row:
            for j in range(m):
                matrix[0][j]=0

        if first_col:
            for i in range(n):
                matrix[i][0]=0


        