class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        temp={}
        ans=0
        for i in nums:
            if i in temp:
                ans+=temp[i]
            temp[i-k]=temp.get(i-k,0)+1
            temp[i+k]=temp.get(i+k,0)+1
        return ans
        
        