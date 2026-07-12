class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        # Next Smaller Element (index) - strictly smaller, scanning right to left
        nse = [n] * n  # default: no smaller element to the right -> boundary is n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)

        # Previous Smaller Element (index) - strictly smaller, scanning left to right
        pse = [-1] * n  # default: no smaller element to the left -> boundary is -1
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)

        max_area = 0
        for i in range(n):
            width = nse[i] - pse[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)

        return max_area