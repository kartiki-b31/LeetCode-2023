class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)

        for i in range(n):
            sum1=sum(nums[:i])
            sum2=sum(nums[i+1:])
            
            if sum1==sum2:
                return i
           
        return -1
        
