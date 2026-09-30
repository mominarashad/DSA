class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hash=[-1]*256

        left=0
        max_len=float("-inf")
        for right in range(len(s)):

            if hash[ord(s[right])]!=-1:
                if hash[ord(s[right])]>=left:
                    left=hash[ord(s[right])]+1

            length=right-left+1
            max_len=max(max_len,length)
            hash[ord(s[right])]=right
            right+=1

        return max_len if max_len!=float("-inf") else 0