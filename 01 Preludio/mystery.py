
import random
import time

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
        if (c>m):
            m=c
            if(array[i] != array[i-1]):
                c=0
    return m


## TEST
arr=[]
for i in range (1,5000):
    arr.append(random.randint(1,50))

start_time = time.time()
print(Mystery(arr))
end_time = time.time()
print('Duration: {}'.format(end_time - start_time))

start_time2 = time.time()
print(MysteryMejor(arr))
end_time2 = time.time()
print('Duration: {}'.format(end_time2 - start_time2))
