class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [n for n in nums if n > 0]
        print(nums)
        nums.sort()
        print(nums)

        target = 1
        '''
        [3, 4, 1]
        [1, 3, 4]
        '''
        for i in nums:
            if i == target:
                target += 1
            elif i > target:
                return target
        
        return target