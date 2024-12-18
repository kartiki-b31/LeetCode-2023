class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m=len(nums1)
        n=len(nums2)

        dp=[[0]*(n+1) for _ in range(m+1)]

        '''
        arr2--->j
        arr1 i |
                |
                i

        '''
        max_len=0
        end_of_arr1=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                    if dp[i][j]>max_len:
                        max_len=dp[i][j]
                        end_of_arr1=i
        
        return max_len
