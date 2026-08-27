class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort()

        first=strs[0]
        last=strs[-1]
        res=""
        for idx,ch in enumerate(first):
            if ch!=last[idx]:
                break
            res+=ch

        return res