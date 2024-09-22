class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        insert=0
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                insert=mid
                end=mid-1
            elif nums[mid]<target:
                insert=mid+1
                start=mid+1
        return insert

                