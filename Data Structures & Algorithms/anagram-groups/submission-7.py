class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups={}

        for words in strs:
            freq={}
            for ch in words:
                if ch in freq:
                    freq[ch]+=1
                else:
                    freq[ch]=1

            
            keys=tuple(sorted(freq.items()))

            if keys in groups:
                groups[keys].append(words)
            else:
                groups[keys]=[words]

        return list(groups.values())
        