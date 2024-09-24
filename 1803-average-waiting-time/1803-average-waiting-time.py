class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        busyuptill=0.0000
        waitingtime=0.0000
        n=len(customers)
        for i in range(len(customers)):
            arrival=customers[i][0]
            time=customers[i][1]
            waitingtime+=(max(arrival,busyuptill)+time-arrival)
            busyuptill=max(arrival,busyuptill) + time
            
        return ((waitingtime*1.0000)/(len(customers)))
   