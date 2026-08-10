class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        if n<4:
            return []
        res=set() #bcz the indices i, j and k are all distinct.
        for i in range(n-3):
            for j in range(i+1,n-2):
                low=j+1
                high=n-1

                while low<high:
                    sum=nums[i]+nums[j]+nums[low]+nums[high]
                    if sum==target:
                        res.add((nums[i],nums[j],nums[low],nums[high]))
                        low+=1
                        high-=1
                    elif sum<target:
                        low+=1
                    else:
                        high-=1

        return [list(triplet) for triplet in res]
        
        