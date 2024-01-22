class Solution:
    def swap(self,nums,a,b):
        temp=nums[a]
        nums[a]=nums[b]
        nums[b]=temp
    
        
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start=0
        mid=0
        end=len(nums)-1
        while(mid<=end):
            if nums[mid]==0:
                self.swap(nums,start,mid)
                start=start+1
                mid=mid+1
                
            elif nums[mid]==1:
                mid=mid+1
                
            else: 
                self.swap(nums,mid,end)
                end=end-1
                
                    
                    
                        