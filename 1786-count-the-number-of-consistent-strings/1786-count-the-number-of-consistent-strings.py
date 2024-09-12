class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_arr=set()
        for i in range(len(allowed)):
            allowed_arr.add(allowed[i])

        print(allowed_arr)
        count=0
        for stringg in words:
            is_consistent=True
            for letter in stringg:
                if letter not in allowed_arr:
                    is_consistent=False
                    break
            if is_consistent:
                count+=1
                
        
        print(count)

        return count