class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        withoutflip=0
        withflip=0
        max_ones=0
        for num in nums:
            if num==1:
                withoutflip+=1
                withflip+=1
            else:
                withflip=withoutflip+1
                withoutflip=0
            
            max_ones=max(max_ones,withflip)
        return max_ones