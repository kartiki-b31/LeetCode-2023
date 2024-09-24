class Solution:
    def isValid(self, s: str) -> bool:
        d={"{":"}","(":")","[":"]"}
        count1=0
        count2=0
        count3=0
        stack=[] #()
        for ch in s:
            if ch=="{" or ch=="(" or ch=="[":
                stack.append(ch)
            elif ch==")" and (len(stack)==0 or stack.pop()!='('):#0 and (0 or 0)
                return False
            elif ch=="}" and (len(stack)==0 or stack.pop()!='{'):#0 and (0 or 0)
                return False
            elif ch=="]" and (len(stack)==0 or stack.pop()!='['):#0 and (0 or 0)
                return False
            
        if len(stack)!=0:
            return False
        else:
            return True
                