class TwoSum:

    def __init__(self):
        self.nums=[]

    def add(self, number: int) -> None:
        self.nums.append(number)
        

    def find(self, value: int) -> bool:
        if len(self.nums)<2:
            return False
        d=defaultdict(int)
        #nums=[1,3,5] #val=4
        #d={1:3,3:1,5:-1}
        for i in range(len(self.nums)):
            comple=value-self.nums[i]
            if comple in d:
                return True
            d[self.nums[i]]=comple
        #print(d)
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)