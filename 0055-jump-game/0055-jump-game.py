class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums) #5
        #[2,3,1,1,4]
        finalpos=n-1 #4
        for i in range(n-1,-1,-1): #4,-1,-1
            if i+nums[i]>=finalpos: #4+4>=4 #3+1>=4 #2+1>=3 #1+3>=2,#0+2>=1
                finalpos=i #finapos=1
        if finalpos==0:
            return True
        else:
            return False