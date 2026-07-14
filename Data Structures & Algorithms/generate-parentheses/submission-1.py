class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        def solve(current,open_brac,closed_brac):

            if len(current)==2*n:
                return res.append(current[:])

            if open_brac<n:
                solve(current+'(',open_brac+1,closed_brac)

            if closed_brac<open_brac:
                solve(current+')',open_brac,closed_brac+1)
            
            return res
        
        return solve("",0,0)