class Solution:
    def reachNumber(self, target: int) -> int:
        #number of steps to target is same as the minimum steps to abs(target)
        '''
        target=5
        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
        (1-2-3+4+5) is equivalent to 
        ((1+2+3+4+5)-2*(2+3))=5(i.e. target)
        (ans(in code))- 2*(m)= target 
        ===> m is multiple of 2
        conclusion: to get a valid output (ans-target) should be divisible by 2
        '''
        ans=0
        k=0
        target=abs(target)
        while ans<target:
            ans+=k
            k+=1
        while (ans-target)%2:
            ans+=k
            k+=1
        return k-1