class Solution:
    def partition(self, s: str) -> List[List[str]]:

            def check_validity(start,end):
                while start<=end:
                    if s[start]!=s[end]:
                        return False

                    start+=1
                    end-=1
                return True

            res=[]

            def solve(index,current):
                
                if index==len(s):
                    return res.append(current[:])

                for i in range(index,len(s)):

                    if check_validity(index,i):
                        current.append(s[index:i+1])
                        solve(i+1,current)
                        current.pop()

                return res

            return solve(0,[])

                
        