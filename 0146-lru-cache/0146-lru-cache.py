class Node:
    def __init__(self,key,value) -> None:
        self.key=key
        self.prev=None
        self.value=value
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dic={}
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        
        node=self.dic[key]
        self.remove(node)
        self.add(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node=self.dic[key]
            self.remove(old_node)
        
        node=Node(key,value)
        self.dic[key]=node
        self.add(node)
        
        if len(self.dic) >self.capacity:
            node_to_delete=self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]
    
    def add(self,node):
        prev_end=self.tail.prev
        prev_end.next=node
        node.prev=prev_end
        node.next=self.tail
        self.tail.prev=node
        
    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)