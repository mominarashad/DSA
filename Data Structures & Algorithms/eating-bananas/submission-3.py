class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        


        def check_hour(hour):
            total_hour=0

            for i in range(len(piles)):
                total_hour+=math.ceil(piles[i]/hour)
            return total_hour


        low=1
        high=max(piles)

        while low<=high:

            mid=(low+high)//2
            
            t_h=check_hour(mid)
            
            if t_h>h:
                low=mid+1
            else:
                high=mid-1

        return low