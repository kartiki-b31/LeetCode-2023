import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i]=nums[i]*(-1)
            
        #print(nums)   
        heapq.heapify(nums)
        ne=-1
        ans=0
        for i in range(k):
            ans=ne*heapq.heappop(nums)
            
        
        return ans