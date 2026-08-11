class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen=set() #to hold only distinct indices
        i=0

        for j in range(i,len(nums)):

            if j-i>k:
                seen.remove(nums[i])
                i+=1

            if nums[j] in seen:
                return True

            seen.add(nums[j])

        return False
        