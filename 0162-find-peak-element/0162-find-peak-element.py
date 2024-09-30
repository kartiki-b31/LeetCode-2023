class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #maxi=max(nums)
        left=0
        right=len(nums)-1
        if len(nums)==1:
            return 0
        #print(right)
        while left<right:
            mid=(left+right) // 2
            print(mid)
            if nums[mid-1]<=nums[mid]>=nums[mid+1]:
                return mid
            elif nums[mid]<nums[mid+1]:
                left=mid+1
            else:
                right=mid
        return mid+1
        

        