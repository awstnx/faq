def Shell(array):
    middle = len(array) // 2
    while middle > 0:
        for i, el in enumerate(array):
            while i >= middle and array[i - middle] > el:
                array[i] = array[i - middle]
                i -= middle
            array[i] = el
        middle = 1 if middle == 2 else int(middle * 5.0 / 11)
    return array

array = [4,7,5,3,6,2,1]
Shell(array)
print(array)