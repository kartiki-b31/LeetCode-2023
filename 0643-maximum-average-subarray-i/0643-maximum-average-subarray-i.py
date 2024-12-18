class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        best=sum(nums[:k])
        now=sum(nums[:k])

        for i in range(k,len(nums)):
            now+=nums[i]-nums[i-k]
            if now>best:
                best=now
        return best/k