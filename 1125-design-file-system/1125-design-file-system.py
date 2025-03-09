class FileSystem:

    def __init__(self):
        self.paths=defaultdict()

    def createPath(self, path: str, value: int) -> bool:
        #step-1 basic path validations
        if path=="/" or len(path)==0 or path in self.paths:
            return False
        
        #step -2 if the parent does not exist. Note "/" is a valid parent.
        parent=path[:path.rfind('/')]
        if len(parent)>1 and parent not in self.paths:
            return False
        
        #step3 add this new path and return True
        self.paths[path]=value
        return True

    def get(self, path: str) -> int:
        return self.paths.get(path,-1)
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)