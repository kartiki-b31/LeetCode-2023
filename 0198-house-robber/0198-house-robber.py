class Solution:
    def rob(self, nums: List[int]) -> int:
        #[2,7,9,3,1]
        #pick i=7,  [not pick i-1, i+1], [can pick i+2, i-2]
        #     2 7 9 3 1
        #dp=[ 0 1 0 1 0 ]
        #dp=[ 1 0 1 0 1 ]
        #dp=[ 2 7 ([i-1],[i+i-2])]
        n=len(nums)
        dp=[0]*n
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n):
            dp[i]=max(dp[i-1],nums[i]+dp[i-2])
            #=max(7,2)
        print(dp)
        return dp[-1]
        
