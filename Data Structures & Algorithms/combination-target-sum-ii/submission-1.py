class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        n=len(candidates)
        res=[]
        def solve(index,current,current_sum):

            if current_sum==target:
                return res.append(current[:])

            if index==n or current_sum>target:
                return None

            current.append(candidates[index])
            solve(index+1,current,current_sum+candidates[index])
            current.pop()

            #remove the duplicates

            j=index+1

            while j<n and candidates[j]==candidates[index]:
                j+=1

            solve(j,current,current_sum)

            return res

        return solve(0,[],0)
        