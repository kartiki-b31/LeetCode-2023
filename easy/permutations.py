
def permutations1(a):
    results=[]
    permutations(a,0, results)
    return results

def permutations(a,start, results):
    if(start >= len(a)):
        results.append(a.copy())
    else:
        for i in range (start,len(a),1):
            swap(a, start, i)
            permutations(a,start+1, results)
            swap(a, start, i)

def swap(a, i ,j):
    temp=a[i]
    a[i]=a[j]
    a[j]=temp
        
print(permutations1([1,2,3]))
