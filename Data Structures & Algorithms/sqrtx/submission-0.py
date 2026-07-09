
class Solution:
    def mySqrt(self, x: int) -> int:

        if x<2:
            return x

        low=0
        high=x
        ans=float("inf")

        while low <=high :
            mid=(low+high)//2

            if mid<=x//mid:
                ans=mid
                low=mid+1
                
            else:
                high=mid-1

        return ans



        
        