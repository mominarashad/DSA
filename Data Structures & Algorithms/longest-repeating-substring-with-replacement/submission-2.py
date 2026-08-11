class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left=0
        hash=[0]*26
        max_window=0
        max_freq=0
        for right in range(len(s)):
            hash[ord(s[right])-ord('A')]+=1

            window=right-left+1
            max_freq=max(max_freq,hash[ord(s[right])-ord('A')])

            if window-max_freq>k:
                hash[ord(s[left])-ord('A')]-=1
                left+=1

            window=right-left+1
            max_window=max(max_window,window)

        return max_window

        