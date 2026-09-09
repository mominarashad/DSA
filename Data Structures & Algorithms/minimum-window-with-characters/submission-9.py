class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        min_len=float("inf")

        freq={}

        for ch in t:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1


        count=len(freq)

        i=0
        j=0

        while j<len(s):

            if s[j] in freq:
                freq[s[j]]-=1

                if freq[s[j]]==0:
                    count-=1

            if count==0:

                while count==0:

                    if s[i] in freq:
                        freq[s[i]]+=1

                        if freq[s[i]]==1:
                            count+=1

                            if j-i+1<min_len:
                                min_len=j-i+1
                                start=i

                    i+=1

            j+=1

        return ("" if min_len==float("inf") else s[start:start+min_len])









