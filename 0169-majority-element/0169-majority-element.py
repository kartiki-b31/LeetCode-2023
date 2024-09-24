class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        x=Counter(nums)
        for k,v in x.items():
            if v>n//2:
                return k
        return 0