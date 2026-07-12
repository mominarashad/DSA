class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n=len(nums)
        result=[0]*(n-k+1)
        dq=deque()

        for i in range(k):

            while dq and nums[dq[-1]]<=nums[i]:
                dq.pop()

            dq.append(i)

        result[0]=nums[dq[0]]

        #process remaining

        for i in range(k,n):

            if dq[0]<=i-k:
                dq.popleft()

            while dq and nums[dq[-1]]<=nums[i]:
                dq.pop()

            dq.append(i)

            result[i-k+1]=nums[dq[0]]

        return result

            
        