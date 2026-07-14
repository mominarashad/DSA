class Solution:
    def maxArea(self, heights: List[int]) -> int:

        water=0

        left=0

        right=len(heights)-1
        while left<=right:
            width=right-left
            length=min(heights[left],heights[right])

            water=max(water,width*length)

            if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1

        return water
        