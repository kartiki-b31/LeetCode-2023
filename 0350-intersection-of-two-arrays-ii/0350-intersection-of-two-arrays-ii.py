class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        
#         for i in range(len(nums1)):
#             for j in range(len(nums2)):
#                 if nums1[i]==nums2[j]:
                    
#                     ans.append(nums1[i])
#                     nums1[i]=-1
#                     nums2[j]=-1
#                     break

                    
                    
        # return ans          
        
        cnt1=Counter(nums1)
        cnt2=Counter(nums2)
        mini=0
        for i in cnt1:
            if i in cnt2:
                mini=min(cnt1[i],cnt2[i])
                
                ans.extend([i]*mini)
            
        
        return ans
        