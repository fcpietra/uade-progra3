def Mystery (array):
    i = 0
    j=0
    c=0
    m=0
    while(i<len(array)):
        if(array[i]==array[j]):
            c+=1
        j+=1
        if(j==len(array)):
            if(c>m):
                m=c
            c=0
            i+=1
            j=i
    return m

def MysteryMejor (array):
    m=0
    c=0
    array.sort()
    for i in array:
        c+=1
        m=c
        if(array[i] != array[i-1]):
            c=0
    return m - 1


## TEST
print(Mystery([2,2,3,3,4,4,4,5,5,5,5,5,5,5,5,5]))
print(MysteryMejor([2,2,3,3,4,4,4,5,5,5,5,5,5,5,5,5,5]))