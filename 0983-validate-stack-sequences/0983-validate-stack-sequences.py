class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    
        stack=[]
        idx1=0
        idx2=0
        while idx1<len(pushed) and idx2<len(popped): #4,1
            stack.append(pushed[idx1])  #1,2,3,5
            while len(stack)!=0 and stack[-1]==popped[idx2]: #5,5,
                stack.pop() #5
                idx2+=1 #2

            idx1+=1 #5

        if len(stack)==0:
            return True
        else:
            return False    
            