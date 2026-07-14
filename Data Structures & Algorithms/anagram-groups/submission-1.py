class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups={}

        for word in strs:
            freq={}
            for ch in word:
                if ch in freq:
                    freq[ch]+=1
                else:
                    freq[ch]=1

            key=tuple(sorted(freq.items()))

            if key in groups:
                groups[key].append(word)
            else:
                groups[key]=[word]

        return list(groups.values())