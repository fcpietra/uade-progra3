def BubbleSort(array):
    for i in range(len(array) - 1, 0, -1):
        for j in range (0, len(array) - 1, 1):
            if j>i:
                break
            elif (array[i] < array[j]):
                aux = array[i]
                array[i]=array[j]
                array[j]=aux
    return array

#TEST
print(BubbleSort([25,5,48,10,26,123,4]))