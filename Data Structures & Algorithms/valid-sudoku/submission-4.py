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

                nums=board[i][j]
                box_id=3*(i//3)+(j//3)

                if nums in rows[i] or nums in cols[j] or nums in box[box_id]:
                    return False

                rows[i].add(nums)
                cols[j].add(nums)
                box[box_id].add(nums)

        return True

        

                