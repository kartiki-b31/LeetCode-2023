class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = list(set(nums))

        nums.sort()

        longest = 0
        length = 0
        prev = -1
        for num in nums:
            if (num-prev)==1:
                length += 1
            else:
                
                length=1
            prev = num
            longest=max(longest,length)
        return longest