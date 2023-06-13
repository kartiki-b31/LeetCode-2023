class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.bigLimit=big
        self.mediumLimit=medium
        self.smallLimit=small
        
        self.parking_array=[None]*(big+medium+small)

    def addCar(self, carType: int) -> bool:
        if carType==1:
            limit=self.bigLimit
        elif carType==2:
            limit=self.mediumLimit
        else:
            limit=self.smallLimit
            
        count=0
        for i in range(len(self.parking_array)):
            if self.parking_array[i]==carType:
                count+=1
            if count==limit:
                return False
            if self.parking_array[i] is None:
                self.parking_array[i]=carType
                return True
            
            
        return False
        
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)