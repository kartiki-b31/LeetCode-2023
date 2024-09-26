class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        for i, n in enumerate(nums1):
            d[n]=i
        res=[-1]*len(nums1)
        stack=[]
        for i in range(len(nums2)):
            cur=nums2[i]
            while stack and cur>stack[-1]:
                val=stack.pop()
                idx=d[val]
                res[idx]=cur
            if cur in d:
                stack.append(cur)
        return res


