class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n=len(board)
        m=len(board[0])

        def solve(row,col,index):

            if index==len(word):
                return True

            if row<0 or col<0 or row>=n or col>=m or board[row][col]!=word[index]:
                return False

            temp=board[row][col]
            board[row][col]='#'

            found=solve(row-1,col,index+1) or solve(row+1,col,index+1) or solve(row,col+1,index+1) or solve(row,col-1,index+1)

            board[row][col]=temp

            return found

        for i in range(n):
            for j in range(m):
                if solve(i,j,0):
                    return True

        return False