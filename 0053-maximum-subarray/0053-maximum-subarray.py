class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #[5,4,-1,7,8],sum+total=23
        #[5,9,8,15,23]
        #[-2,1,-3,4,-1,2,1,-5,4]
        #         l
        #            r
        #if neg: dont check
        #if sum get negative
        #max_sum=max(maxsum,sum(l to r))
        n=len(nums)
        left=0
        right=0
        maxsum=0
        sum_total=0
        
        while left<=right and left<n and right<n:
            sum_total+=nums[right]
            if sum_total<0:
                right+=1
                left=right
                sum_total=0
            else:
                maxsum=max(maxsum,sum_total)
                right+=1
        
        if maxsum==0:
            return max(nums)
        return maxsum

