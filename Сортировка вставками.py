def InsertionSort(array):
    for i in range(1, len(array)):
        key= array[i]
        j = i-1
        while j>=0 and key<array[j]:
           array[j+1]=array[j]
           j=j-1
        array[j+1]=key
        
array=[12,19,13,15,6]
insertionSort(array)
for i in range(len(array)):
    print(array[i])
