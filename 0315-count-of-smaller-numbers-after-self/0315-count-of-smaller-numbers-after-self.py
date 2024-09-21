class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr)<=1:
                return arr
            
            mid=len(arr)//2
            left=merge_sort(arr[:mid])
            right=merge_sort(arr[mid:])

            i=0 #left arr index
            j=0 # right arr index
            k=0 #orignal arr index
            count=0
            temp=[]
            #traverse through left and right array to chekc the elemenet
            while i<len(left) and j<len(right):
                if left[i][1]<=right[j][1]:
                    arr[k]=left[i]
                    counts[left[i][0]]+=count
                    i+=1
                else:
                    arr[k]=right[j]
                    count+=1
                    j+=1
                k+=1
            #if there will be any element left in the left array
            while i<len(left):
                arr[k]=left[i]
                counts[left[i][0]]+=count
                i+=1
                k+=1
            
            #if there are any elements in the right array
            while j<len(right):
                arr[k]=right[j]
                j+=1
                k+=1
            
            return arr
        
        arr=list(enumerate(nums))
        counts=[0]*len(arr)
        merge_sort(arr)
        return counts