class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        index=0
        answer=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    index=j
                    break
            added=False
            for k in range(index, len(nums2)):
                if nums2[index]<nums2[k]:
                    answer.append(nums2[k])
                    added=True
                    break
            if not added:
                answer.append(-1)
                
        return answer
        
        