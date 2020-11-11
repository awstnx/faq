import random

def sort(nums, first, last):
    if first >= last:
        return array

    i = first
    j = last
    pivot = array[random.randint(first, last)]

    while i <= j:
        while array[i] < pivot: i += 1
        while array[j] > pivot: j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i = i + 1
            j = j - 1
    sort(nums, first, j)
    sort(nums, i, last)



array = [1,6,5,8,9,7,3,2,4]
sort(array, 0, len(array)-1)
print(array)
