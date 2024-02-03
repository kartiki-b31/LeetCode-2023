class Solution:
    def jump(self, nums: List[int]) -> int:
        totalJumps=0
        destination=len(nums)-1
        coverage=0
        lastJumpidx=0
        if(len(nums)==1):
            return 0
        
        for i in range(len(nums)):
            coverage=max(coverage,i+nums[i])
            if i==lastJumpidx:
                lastJumpidx=coverage
                totalJumps+=1
                
                if coverage>=destination:
                    return totalJumps
                
                
        
        
        return totalJumps
        