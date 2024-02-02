class Solution:
    def canJump(self, nums: List[int]) -> bool:
        finalposition=len(nums)-1
        for idx in range(len(nums)-1,-1,-1):
            if idx+nums[idx]>=finalposition:
                finalposition=idx
                
        return True if finalposition == 0 else False
        