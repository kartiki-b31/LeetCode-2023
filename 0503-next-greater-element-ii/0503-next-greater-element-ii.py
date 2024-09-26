class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        n=len(nums)
        res=[-1]*n
        for i in range(0,n*2):
            while stack and nums[i%n]>nums[stack[-1]]:
                idx=stack.pop()
                res[idx]=nums[i%n]
        
            stack.append(i%n)
        return res