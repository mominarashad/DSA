class Solution:
    def minWindow(self, s: str, t: str) -> str:

        freq_t=[0]*256
        freq_s=[0]*256

        for ch in t:
            freq_t[ord(ch)]+=1

        def contain(freq_t,freq_s):
            for ch in t:
                if freq_t[ord(ch)]>freq_s[ord(ch)]:
                    return False
            return True

        result=""
        left=0
        min_len=float("inf")
        for right in range(len(s)):

            while left<len(s) and not contain(freq_t,freq_s):
                freq_s[ord(s[left])]+=1
                left+=1

            if min_len>left-right+1 and contain(freq_t,freq_s):
                result=s[right:left]
                min_len=left-right+1
                
            freq_s[ord(s[right])]-=1
        return result




         