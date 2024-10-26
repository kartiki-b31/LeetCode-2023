class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        max_sum=-float('inf')
        cur_sum=0
        [-2,7,-3,4]
        i,j
        ans=0
        cur_sum=0
        if nums[i]>max_sum:
            max_sum=nums[i]

            cur_sum=-2

        '''

        n=len(nums)
        max_sum=-float('inf')

        cur_sum=0
        for i in range(n): #-2+7=5
            cur_sum=nums[i]+cur_sum
            max_sum=max(cur_sum,max_sum)
            if cur_sum<0:
                cur_sum=0
            

        return max_sum