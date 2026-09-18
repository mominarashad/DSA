import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def total_hour(hour):

            total_h=0

            for i in range(len(piles)):
                total_h+=math.ceil(piles[i]/hour)

            return total_h

        low=1
        high=max(piles)

        while low<=high:

            mid=(low+high)//2

            t_h=total_hour(mid)

            if t_h>h:
                low=mid+1
            else:
                high=mid-1

        return low

        