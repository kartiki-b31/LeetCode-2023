class Solution:
    def compress(self, chars: List[str]) -> int:
        idx=0 #to modify char in place
        n=len(chars)
        i=0 #pointer to traverse through chars
        while i<n:
            char=chars[i]
            count=0
            #count consecutive occurrance of chars[i]
            for j in range(i,n):
                if chars[j]==char:
                    count+=1
                else:
                    break
            chars[idx]=char
            idx+=1

            if count>1:
                for digit in str(count):
                    chars[idx]=digit
                    idx+=1
            i+=count
        return idx


