class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        unitCount = 0
        remainingTruckSize = truckSize
        while remainingTruckSize > 0:
            maxUnitBoxIndex = self.findMaxUnitBox(boxTypes)
            # check if all boxes are used
            if maxUnitBoxIndex == -1:
                break
            # find the box count that can be put in the truck
            boxCount = min(remainingTruckSize, boxTypes[maxUnitBoxIndex][0])
            unitCount += boxCount * boxTypes[maxUnitBoxIndex][1]
            remainingTruckSize -= boxCount
            # mark the box with index maxUnitBoxIndex as used
            boxTypes[maxUnitBoxIndex][1] = -1
        return unitCount

    def findMaxUnitBox(self, boxTypes):
        maxUnitBoxIndex = -1
        maxUnits = 0
        for i in range(len(boxTypes)):
            if boxTypes[i][1] > maxUnits:
                maxUnits = boxTypes[i][1]
                maxUnitBoxIndex = i
        return maxUnitBoxIndex
