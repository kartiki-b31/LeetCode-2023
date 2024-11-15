#[[100, 200], [1000, 1250], [200, 1300], [2000, 3200]]

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:

        courses.sort(key=lambda x:x[1])
        print(courses)

        maxHeap=[]
        nums=[100,1000,200,2000]
        
        t=0
        for i in range(len(courses)):
            t+=courses[i][0]
            if t<=courses[i][1]:
                heappush(maxHeap,-courses[i][0])
                heapq.heapify(maxHeap)
                #print(t)
            elif t>courses[i][1]:
                #print(t)
                #print(courses[i][1])
                heappush(maxHeap,-courses[i][0])
                t=t+heapq.heappop(maxHeap)
                heapq.heapify(maxHeap)
                #print(maxHeap)

                
        #print(t)
        #print(maxHeap)
        #print(-heapq.heappop(maxHeap))
        

        return len(maxHeap)
        