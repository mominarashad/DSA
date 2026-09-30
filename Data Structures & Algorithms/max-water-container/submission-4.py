class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        low=0

        high=len(heights)-1

        max_water=0

        while low<=high:

            length=min(heights[low],heights[high])
            width=high-low

            max_water=max(max_water,width*length)

            if heights[low]<heights[high]:
                low+=1
            else:
                high-=1

        return max_water