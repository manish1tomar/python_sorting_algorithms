def twoNumberSum(array, targetSum):
    ret_array = []
    dict = {}
    other_num = targetSum
    element = None

    for i in array:
        dict[i] = 'Found'

    for i in array:
        other_num = targetSum - i
        if other_num != i:
            if other_num in dict:
                element = [i, other_num]
                element.sort()
                if element not in ret_array:
                    ret_array.append(element)
    
    return ret_array

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6],10))
a = [11,-1]
a.sort()
print(a)