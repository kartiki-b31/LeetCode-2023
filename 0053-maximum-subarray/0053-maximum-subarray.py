class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
#         ans=[]
        
#     #Ratto_automatic
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)+1):
#                 ans.append(sum(nums[i:j]))

               
#         return max(ans)
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
        