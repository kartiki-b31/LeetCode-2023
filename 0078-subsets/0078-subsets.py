class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def recursive(subset,i):
            if len(nums)==i:
                ans.append(subset[:])
                return 
                
            subset.append(nums[i])
            recursive(subset,i+1)
            subset.pop()
            recursive(subset,i+1)



        subset=[]
        ans=[]
        recursive(subset,0)
        return ans
