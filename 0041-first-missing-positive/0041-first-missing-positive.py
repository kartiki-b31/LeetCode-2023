class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        seen=[False]*(n+1)
        #print(seen)
        for num in nums:
            if 0<num<=n:
                seen[num]=True
        #print(seen)
        for i in range(1,n+1):
            if not seen[i]:
                return i
        return n+1
        '''
        nums_set=sorted(nums)
        n=len(nums_set)
        # max_num=max(nums_set)
        # min_num=min(nums_set)
        # print(max_num)
        # print(min_num)
        print(nums_set)
        #[7, 8, 9, 11, 12]
        if n==1:
            if nums[0]<1:
                return 1
            elif nums[0]==1:
                return 2
        #[-1, 1, 3, 4]
        for i in range(n):
            print(nums_set[i])

            if nums_set[i]!=i+1:
                return i+1
        return n
        '''