#Time O(nlogn), Space O(n)
def sortedSquaredArray(array):
    arr = []
    for i in array:
        arr.append(i*i)
    arr.sort()
    return arr

#Time O(nlogn), Space O(n)
def sortedSquaredArray_(array):
    return sorted([i*i for i in array])

#Time O(n), Space O(n)
def sortedSquaredArray(array):
    result = [0 for i in array]
    start = 0
    end = len(array) -1
    while end > start:
     
        if abs(array[end]) > abs(array[start]):
            result[end] = array[end]**2
            end -= 1
        else:
            result[end] = array[start]**2
            start += 1
    result[0] = array[start]**2
    return result
