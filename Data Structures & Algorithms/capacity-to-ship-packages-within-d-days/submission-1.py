class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def find_capacity(capacity):
            day=1
            load=0

            for w in weights:
                if load+w >capacity:
                    day+=1
                    load=0
                
                load+=w

            return day<=days

        low=max(weights)
        high=sum(weights)

        while low<high:

            mid=(low+high)//2

            if find_capacity(mid):
               high= mid
            else:
                low=mid+1

        return low
            
            

            
        