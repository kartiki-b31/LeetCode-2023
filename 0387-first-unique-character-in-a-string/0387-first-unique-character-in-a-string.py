class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=Counter(s)
        for idx, ch in enumerate(s):
            if count[ch]==1:
                return idx
        return -1