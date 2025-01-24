class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        nums=colors+colors
        n=len(nums)
        count=0
        for i in range(len(colors)):
            if nums[i]==nums[i+2] and nums[i]!=nums[i+1]:
                count+=1
            
        return count