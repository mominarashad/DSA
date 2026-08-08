class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums)<=1:
            return nums

        n=len(nums)

        mid=n//2

        first=self.sortArray(nums[:mid])
        last=self.sortArray(nums[mid:])

        def merge(first,second):

            i=0
            j=0
            res=[]

            while i<len(first) and j<len(last):
                if first[i]<=last[j]:
                    res.append(first[i])
                    i+=1
                else:
                    res.append(last[j])
                    j+=1

            while i<len(first):
                res.append(first[i])
                i+=1
            while j<len(last):
                res.append(last[j])
                j+=1

            return res

        return merge(first,last)


        
        