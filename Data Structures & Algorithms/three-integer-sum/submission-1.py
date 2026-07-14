class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)

        if n<3:
            return []

        res=set()

        for i in range(n-2):
            low=i+1
            high=n-1

            while low<high:

                sum= nums[i]+nums[low]+nums[high]
                if sum==0:
                    res.add((nums[i],nums[low],nums[high]))
                    low+=1
                    high-=1
                elif sum<0:
                    
                    low+=1
                else:
                    high-=1
                    

                
        return [list(triple) for triple in res]
        