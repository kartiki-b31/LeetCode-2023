from collections import Counter
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
#         answer1=[]
#         answer2=[]
#         answer=[]
        
#         test_nums1 = list(set(nums1))
#         test_nums2 = list(set(nums2))
        # print(test_nums1)
        # print(test_nums2)
        # print(list(set(nums1)-set(nums2)))
        # print(list(set(nums2)-set(nums1)))
        
#         for i in range(len(test_nums1)):
#             if test_nums1[i] not in test_nums2:
#                 answer1.append(test_nums1[i])
#                 #print(answer1)
                
        
#         for i in range(len(test_nums2)):
#             if test_nums2[i] not in test_nums1:
#                 answer2.append(test_nums2[i])
#                 #print(answer2)
            
#         answer.append(answer1)
#         answer.append(answer2)
        #[1,3]
        #[4,6]
        #[[1,3]]
        
        
        
        return list(set(nums1)-set(nums2)),list(set(nums2)-set(nums1))
       