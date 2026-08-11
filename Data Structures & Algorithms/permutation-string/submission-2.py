class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s=len(s1)
        t=len(s2)

        if s>t:
            return False

        hash_s1=[0]*26
        hash_s2=[0]*26

        for i in range(s):
            hash_s1[ord(s1[i])-ord('a')]+=1
            hash_s2[ord(s2[i])-ord('a')]+=1


        if hash_s1==hash_s2:
            return True

        
        for j in range(s,t):
            hash_s2[ord(s2[j])-ord('a')]+=1
            hash_s2[ord(s2[j-s])-ord('a')]-=1

            if hash_s1==hash_s2:
                return True

        return False


            


        


        