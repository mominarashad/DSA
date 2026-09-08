class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len=0
        hash_map=[-1]*256
        left=0

        for right in range(len(s)):

            if hash_map[ord(s[right])]!=-1:
                if hash_map[ord(s[right])]>=left:
                    left=hash_map[ord(s[right])]+1

            length=right-left+1
            max_len=max(max_len,length)
            hash_map[ord(s[right])]=right
        
        return max_len

       
            
            
        