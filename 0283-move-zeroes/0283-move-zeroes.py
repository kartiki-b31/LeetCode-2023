class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        0,1,0,3,12
        i=0,j=0
        0,0,1,3,12
        i=0,j=0
        """
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                nums.remove(nums[i])
                nums.append(0)
        return nums

        