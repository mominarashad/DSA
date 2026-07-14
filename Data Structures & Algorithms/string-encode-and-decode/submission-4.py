class Solution:

    def encode(self, strs: List[str]) -> str:

        encoding=""
        for ch in strs:
            encoding+=str(len(ch))+'#'+ch

        return encoding

    def decode(self, s: str) -> List[str]:

        i=0 
        n=len(s)
        res=[]

        while i<n:
            j=i

            while s[j]!='#':
                j+=1

            length=int(s[i:j])
            start=j+1

            res.append(s[start:start+length])
            i=length+start

        return res

        
