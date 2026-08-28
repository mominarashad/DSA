class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        box=[set() for _ in range(9)]


        n=len(board)
        m=len(board[0])

        for i in range(n):
            for j in range(m):

                if board[i][j]==".":
                    continue

                num=board[i][j]
                box_id=3*(i//3)+(j//3)

                if num in rows[i] or num in cols[j] or num in box[box_id]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                box[box_id].add(num)

        return True
        

       
                