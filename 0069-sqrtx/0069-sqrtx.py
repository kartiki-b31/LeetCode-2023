class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        left=0
        right=x
        
        while(left<=right):
            mid=(left+right)//2
            if x==mid*mid:
                return mid
            if x<mid*mid:
                right=mid-1
            elif x>mid*mid:
                left=mid+1

        return right
        