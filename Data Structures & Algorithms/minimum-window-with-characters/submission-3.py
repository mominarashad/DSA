class Solution:
    def minWindow(self, s: str, t: str) -> str:

        freq_s=[0]*256
        freq_t=[0]*256

        for ch in t:
            freq_t[ord(ch)]+=1

        def contain(freq_t,freq_s):
            for ch in t:
                if freq_t[ord(ch)]>freq_s[ord(ch)]:
                    return False
            return True

        result=""
        min_len=float("inf")

        right=0

        for left in range(len(s)):

            while right<len(s) and not contain(freq_t,freq_s):
                freq_s[ord(s[right])]+=1
                right+=1

            if right-left+1<min_len and contain(freq_t,freq_s):
                result=s[left:right]
                min_len=right-left+1
            
            freq_s[ord(s[left])]-=1
        return result

            

        