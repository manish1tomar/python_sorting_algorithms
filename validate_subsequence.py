def isValidSubsequence(array, sequence):
    print(array, sequence)
    dict = {}
    idx = None
    for i,j in enumerate(array):
        if j in dict:
            l = dict[j]
            l.extend([i])
            dict[j] = l
        else:
            dict[j] = [i]
    
    if len(sequence) > len(array):
        return False
    elif sequence == array:
        return True
    elif len(array) > 0 and len(sequence) == 0:
        return False

    for i,j in enumerate(sequence):
        if j not in dict:
            return False
        else:
            if idx is None:
                idx = dict[j][0]
                if len(dict[j]) == 1:
                    del(dict[j])
                else:
                    dict[j].pop(0)
            
            elif idx > dict[j][0]:
                return False

            else:
                idx = dict[j][0]
                if len(dict[j]) == 1:
                    del(dict[j])
                else:
                    dict[j].pop(0)  
                              
    return True

print(isValidSubsequence( [1, 1, 1, 1, 1], [1, 1, 1] ))
print(isValidSubsequence( [5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 22, 6, -1, 8, 10] ))
print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 25, 22, 6, -1, 8, 10]))
print(isValidSubsequence([1, 1, 6, 1], [1, 1, 1, 6]))