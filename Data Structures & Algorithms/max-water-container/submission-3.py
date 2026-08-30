class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n=len(heights)
        low=0
        high=n-1
        max_water=0
        while low<=high:

            width=abs(high-low)
            length=min(heights[high],heights[low])

            max_water=max(max_water,(length*width))

            if heights[low]<heights[high]:
                low+=1
            else:
                 high-=1
        
        return max_water



        