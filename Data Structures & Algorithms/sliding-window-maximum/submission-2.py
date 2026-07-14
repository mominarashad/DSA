class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        dq=deque()
        result=[0]*(n-k+1)
        for i in range(k):
            
            while dq and nums[i]>=nums[dq[-1]]:

                dq.pop()
            dq.append(i)
            
        result[0]=nums[dq[0]]

        for i in range(k,n):

            if dq[0]<=i-k:
                dq.popleft()

            while dq and nums[i]>=nums[dq[-1]]:

                dq.pop()
            dq.append(i)
            
            result[i-k+1]=nums[dq[0]]

        return result


            

        