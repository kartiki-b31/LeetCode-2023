class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''

        abcabcbb
          l
              r
        '''
        repeat=set()
        n=len(s)
        l=0
        r=0
        res=0
        for r in range(n):#r=0,1,2,3,4
            #print("inside for",r)
            while s[r] in repeat:#s[3]=a, s[4]=b,c
                repeat.remove(s[l]) #s[l]=a,s[l]=b,c
                #print("inside whil",repeat)
                l+=1 #1,2,3
            repeat.add(s[r])
            #print("after adding",repeat)
            res=max(res,r-l+1)

        return res
