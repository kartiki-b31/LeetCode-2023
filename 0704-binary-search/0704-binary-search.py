
import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)
        
        while(l<h):
            mid=int((l+h)/2)
            if(target == nums[mid]):
                return mid
            if(target<nums[mid]):
                h=mid
            else:
                l=mid+1
        
        return -1