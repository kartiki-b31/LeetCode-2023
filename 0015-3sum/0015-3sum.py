class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def getSum(s, i):
            d = set()
            lst = []
            for n in range(i, len(nums)):
                x = nums[n]
                if s-x in d:
                    lst.append([s-x, x, -s])
                d.add(x)
            return lst
        ans = set()
        for i in range(len(nums)):
            if i and nums[i-1] == nums[i]:
                continue
            lst = getSum(-nums[i], i+1)
            for arr in lst:
                ans.add(tuple(sorted(arr)))
        
        return ans
