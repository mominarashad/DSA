class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)

        if n<4:
            return []

        res=set()

        for i in range(n-3):

            for j in range(i+1,n-2):

                low=j+1
                high=n-1

                while low<high:

                    sum=nums[low]+nums[high]+nums[i]+nums[j]

                    if sum==target:
                        res.add((nums[low],nums[high],nums[i],nums[j]))
                        low+=1
                        high-=1

                    elif sum>target:
                        high-=1
                    else:
                        low+=1

        return [list(quad) for quad in res]
