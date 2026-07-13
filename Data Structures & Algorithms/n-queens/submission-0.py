class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board=[['.']*n for _ in range(n)]

        ans=[]

        placedCol=set()
        placedPos=set()
        placedNeg=set()

        def solve(index):

            if index==n:

                copy=board[:]
                sol=[]

                for c in copy:
                    sol.append("".join(c[:]))

                ans.append(sol)

            for c in range(n):

                if c in placedCol or index+c in placedPos or index-c in placedNeg:
                    continue

                board[index][c]='Q'
                placedCol.add(c)
                placedPos.add(index+c)
                placedNeg.add(index-c)

                solve(index+1)

                board[index][c]='.'
                placedCol.remove(c)
                placedPos.remove(index+c)
                placedNeg.remove(index-c)

            return ans
        return solve(0)


        