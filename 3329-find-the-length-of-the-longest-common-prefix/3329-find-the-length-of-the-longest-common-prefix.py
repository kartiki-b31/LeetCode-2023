class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
    def lcp_length(self,word):
        curr=self.root
        length=0
        for c in word:
            if c not in curr.children:
                return length
            length+=1
            curr=curr.children[c]
        return length

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie=Trie()
        for word in arr1:
            trie.insert(str(word))
        
        longest=0
        for word in arr2:
            longest=max(longest,trie.lcp_length(str(word)))
        
        return longest
        