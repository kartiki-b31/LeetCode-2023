class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels=set()
        vowels.add("a")
        vowels.add("e")
        vowels.add("i")
        vowels.add("o")
        vowels.add("u")

        l=False
        r=False
        count=0
        if left==right:
            if words[left][0] in vowels:
                #print("yes")
                l=True
            if words[left][-1] in vowels:
                #print("right")
                r=True
            
            if l and r:
                count+=1

        if left!=right:
            i=left
            while i<=right:
                l=False
                r=False
                if words[i][0] in vowels:
                    print(i)
                    print("yes")
                    l=True
                if words[i][-1] in vowels:
                    print(i)
                    print("right")
                    r=True
                
                if l and r:
                    count+=1
                i+=1
            
        #print(count)
        return count
