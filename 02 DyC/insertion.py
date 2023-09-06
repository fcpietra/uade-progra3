def Merge(array,ini, fin):
    w=list(range(0, fin-ini))
    mid = (ini+fin) // 2
    i = ini
    j = mid-1
    for k in range(0,fin-ini,1):
        if(j>fin) or (array[i] <= array[j] and i < mid +1):
            w[k] = array[i]
            i+=1
        else:
            w[k] = array[j]
            j+=1

    return array

def MergeSort(array, ini, fin):
    print ("", array)
    if (ini<fin):
        mid = (ini+fin) // 2
        MergeSort(array, ini, mid)
        MergeSort(array, mid+1,fin)
        Merge(array,ini, fin)

    return array

#TEST
array = [25,5,48,10,26,123,4]
print(MergeSort(array, 0, len(array)))