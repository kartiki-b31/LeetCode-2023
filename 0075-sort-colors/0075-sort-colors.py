class Solution:
    def swap(self, arr,i,j):
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         cnt0=0
#         cnt1=0
#         cnt2=0
#         arr=[]
        
#         for i in range(len(nums)):
#             if nums[i]==0:
#                 cnt0=cnt0+1
#             elif nums[i]==1:
#                 cnt1=cnt1+1
#             else:
#                 cnt2=cnt2+1
                
#         for i in range(cnt0):
#             nums[i]=0
        
#         for i in range(cnt0,cnt0+cnt1):
#             nums[i]=1
            
#         for i in range(cnt0+cnt1,len(nums)):
#             nums[i]=2
            
        
#         return nums

        low=0
        mid=0
        high=len(nums)-1
        while(mid<=high):
            if nums[mid]==0:
                self.swap(nums,low,mid)
                low=low+1
                mid=mid+1
            elif nums[mid]==1:
                mid=mid+1
            
            else:
                self.swap(nums,mid,high)
                high=high-1
        