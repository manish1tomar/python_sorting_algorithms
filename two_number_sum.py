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
                if i not in ret_array:
                    ret_array.extend((i, other_num))
    
    return ret_array
