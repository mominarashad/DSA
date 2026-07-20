class Solution:
    def longestPalindrome(self, s: str) -> str:

        start=0
        max_len=1
        n=len(s)
        for i in range(n):

            #odd case
            low=i
            high=i

            while low>=0 and high<n and s[low]==s[high]:
                curr_len=high-low+1
                if curr_len>max_len:
                    start=low
                    max_len=curr_len
                low-=1
                high+=1

            #even case
            low=i
            high=i+1

            while low>=0 and high<n and s[low]==s[high]:
                curr_len=high-low+1
                if curr_len>max_len:
                    start=low
                    max_len=curr_len
                low-=1
                high+=1

        return s[start:start+max_len]

            