class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorval=len(nums)
        for i in range(len(nums)):
            xorval^=i^nums[i]

        return xorval
