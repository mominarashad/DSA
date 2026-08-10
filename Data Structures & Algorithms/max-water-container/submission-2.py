class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        water=0
        low=0
        high=len(heights)-1

        while low<high:
            width=abs(low-high)
            length=min(heights[low],heights[high])

            water=max(water,length*width)

            if heights[low]<heights[high]:
                low+=1
            else:
                high-=1

            

        return water