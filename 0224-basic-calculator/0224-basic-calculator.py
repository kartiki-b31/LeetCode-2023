class Solution:
    def calculate(self, s: str) -> int:
        sign=1 #positive
        sum_arr=0
        num=0
        stack=[]
        for char in s:
            if char.isdigit():
                num=num*10+int(char)
            elif char=="+" or char=="-":
                sum_arr+=sign*num
                num=0
                if char=="+":
                    
                    sign=1
                elif char=="-":
                    sign=-1
            elif char=="(":
                stack.append(sum_arr)
                stack.append(sign)
                sum_arr=0
                sign=1
            elif char==")":
                sum_arr+=sign*num
                num=0
                sum_arr=sum_arr*stack.pop()+stack.pop() #doubt

        
        sum_arr+=sign*num
        #print(sum_arr)
        
        return sum_arr

        