class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        MOD=int(1e9)+7
        n=len(nums)
        total=sum(nums)

        if abs(target) > total or (target+total)%2!=0:
            return 0

        t=(target+total)//2

        dp=[[0]*(t+1) for _ in range(n+1)]

        dp[0][0]=1

        for i in range(1,n+1):
            for j in range(t+1):
                if nums[i-1]<=j:
                    dp[i][j]=(dp[i-1][j]+dp[i-1][j-nums[i-1]])%MOD
                else:
                    dp[i][j]=(dp[i-1][j])%MOD

        return dp[n][t]
        