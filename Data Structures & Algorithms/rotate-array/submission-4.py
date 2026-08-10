class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n=len(nums)

        def reverse(low,high):
            while low<=high:
                nums[low],nums[high]=nums[high],nums[low]
                low+=1
                high-=1


      
        k=n-k
        k=k%n

        reverse(0,k-1)
        reverse(k,n-1)
        reverse(0,n-1)