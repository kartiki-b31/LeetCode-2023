class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]

        def recursive(curr_subset,idx):

            if idx>=len(nums):
                ans.append(curr_subset)
                return
            #no pick # not picking current indiex and movieng to th next
            recursive(curr_subset,idx+1)
            #yes pick
            recursive(curr_subset+[nums[idx]],idx+1)



        curr_subset=[]
        recursive(curr_subset,0)
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
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
        '''
