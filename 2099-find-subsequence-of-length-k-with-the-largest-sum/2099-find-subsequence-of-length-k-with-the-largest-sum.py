import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        n = len(nums)
        for i in range(n):
            heapq.heappush(maxHeap, [-nums[i], i])
        output = []
        for i in range(k):
            output.append(heapq.heappop(maxHeap))
            output[i][0] = -output[i][0]
        output.sort(key=lambda x: x[1])
        return [x for x, y in output]