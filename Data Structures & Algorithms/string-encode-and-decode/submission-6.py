class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding=""
        for ch in strs:
            encoding+=str(len(ch))+'#'+ch

        return encoding


    def decode(self, s: str) -> List[str]:

        i=0
        res=[]
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1

            length=int(s[i:j])
            value=j+1

            res.append(s[value:value+length])
            i=value+length

        return res

            

