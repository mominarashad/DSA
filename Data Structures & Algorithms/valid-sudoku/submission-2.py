class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=len(board)
        m=len(board[0])
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]

        for i in range(n):
            for j in range(m):

                if board[i][j]=='.':
                    continue
                
                nums=board[i][j]
                boxes_id=3*(i//3)+(j//3)

                if nums in rows[i] or nums in cols[j] or nums in boxes[boxes_id]:
                    return False

                rows[i].add(nums)
                cols[j].add(nums)
                boxes[boxes_id].add(nums)

        return True
        
        