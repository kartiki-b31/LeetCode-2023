class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        #[1,4,3,3,2]
        #[1,2,0,0,0]
        #[2,3,3,4,1]
        #[1,2,1,2,0]
        #inc=[0]*n
        #dec=[0]*n
        #[1,1,5]
        count=1
        if (all(x == nums[0] for x in nums)):
            return 1
        rev_nums=nums[::-1]
        max_len=0
        for i in range(n-1):
            if nums[i]<nums[i+1]:
                count+=1
            else:
                count=1
            max_len=max(count,max_len)
        #print(max_len)
        count2=1
        max_len2=0
        for i in range(n-1):
            if rev_nums[i]<rev_nums[i+1]:
                count2+=1
            else:
                count2=1
            max_len2=max(count2,max_len2)
        #print(max_len2)

        return max(max_len,max_len2)
