class Solution:
    def isHappy(self, n: int) -> bool:
        def num_sq(str_n):

            val=0
            for dig in str(str_n):
                squared=(int(dig))**2
                val+=squared
        
            return val

        if n==1:
            return True
        if n==4:
            return False
        return self.isHappy(num_sq(n))