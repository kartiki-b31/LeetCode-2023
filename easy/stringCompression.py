def Compress(s1):
    out=""
    sum=1
    for i in range(len(s1)-1):
        if s1[i]==s1[i+1]:
            sum=sum+1
        else:
            out=out+s1[i]+str(sum)
            sum=1

    out=out+s1[len(s1)-1]+str(sum)
    return out if len(out) <len(s1) else s1



print(Compress("aaabb"))