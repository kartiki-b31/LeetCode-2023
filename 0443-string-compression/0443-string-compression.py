class Solution:
    def compress(self, chars: List[str]) -> int:
        stack=[] #(char,freq)
        for char in chars:
            if stack and stack[-1][0]==char:
                stack[-1]=(char,stack[-1][1]+1)
            else:
                stack.append((char,1))
        
        print(stack)
        ans=0
        for char, count in stack:
            chars[ans]=char
            ans+=1
            if count>1:
                for digit in str(count):
                    chars[ans]=digit
                    ans+=1
        return ans
