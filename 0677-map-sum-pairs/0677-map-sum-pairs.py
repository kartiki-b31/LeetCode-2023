class TrieNode:
    def __init__(self):
        self.children={}
        self.score=0

class MapSum:

    def __init__(self):
        self.root=TrieNode()
        self.map={}
        

    def insert(self, key: str, val: int) -> None:
        my_score=self.map.get(key,0) #existing 3
        delta=val-my_score #delta=2-3
        self.map[key]=val
        cur=self.root

        cur.score+=delta
        for c in key:
            cur=cur.children.setdefault(c,TrieNode())
            cur.score+=delta
        #print(cur.score)
        

    def sum(self, prefix: str) -> int:
        cur=self.root
        total_score=0
        for c in prefix:
            if c not in cur.children:
                return 0
            cur=cur.children[c]

        return cur.score


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)