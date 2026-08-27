class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums)<=1:
            return nums

        
        n=len(nums)

        mid=n//2

        first_half=self.sortArray(nums[:mid])
        second_half=self.sortArray(nums[mid:])

        def merge(first_half,second_half):
            i=0
            j=0
            res=[]

            while i<len(first_half) and j<len(second_half):

                if first_half[i]<=second_half[j]:
                    res.append(first_half[i])
                    i+=1
                else:
                    res.append(second_half[j])
                    j+=1

            while i<len(first_half):
                    res.append(first_half[i])
                    i+=1

            while j<len(second_half):
                    res.append(second_half[j])
                    j+=1

            return res

        return merge(first_half,second_half)
        
        



