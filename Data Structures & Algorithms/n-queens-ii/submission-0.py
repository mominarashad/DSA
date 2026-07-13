class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:

        
        count=0

        placedCol=set()
        placedPos=set()
        placedNeg=set()

        def solve(index):
            nonlocal count
            if index==n:
                count+=1
                return

            for c in range(n):

                if c in placedCol or index+c in placedPos or index-c in placedNeg:
                    continue

                
                placedCol.add(c)
                placedPos.add(index+c)
                placedNeg.add(index-c)

                solve(index+1)

                
                placedCol.remove(c)
                placedPos.remove(index+c)
                placedNeg.remove(index-c)

            return count
        return solve(0)


        