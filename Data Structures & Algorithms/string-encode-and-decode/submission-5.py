class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded=""

        for ch in strs:
            encoded+=str(len(ch))+"#"+ch
            
        return encoded

    def decode(self, s: str) -> List[str]:

        i=0

        n=len(s)

        res=[]

        while i<n:
            j=i
            while s[j]!="#":
                j+=1

            length=int(s[i:j])
            start=j+1

            res.append(s[start:start+length])
            i=start+length

        return res


