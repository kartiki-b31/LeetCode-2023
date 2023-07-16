class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxi=float("-infinity")
        sums=0
        for i in range(len(nums)):
            sums += nums[i]

            if sums > maxi:
                maxi = sums

        # If sum < 0: discard the sum calculated
            if sums < 0:
                sums = 0
                
                
        return maxi
        