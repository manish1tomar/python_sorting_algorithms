def quicksort(list):
    j = len(list) -1
    i = 1
    while True:
        if i <= j:
            if list[i] > list[0]:
                if list[j] < list[0]:
                    list[i], list[j] = list[j], list[i]
                j-=1
            i+=1
        else:
            if list[0] > list[j]:
                list[0], list[j] = list[j], list[0]
            else:
                j = 0
            if len(list[0:j]) > 1:
                list[0:j] = quicksort(list[0:j])
            if len(list[j+1:]) > 1:
                list[j+1:] = quicksort(list[j+1:])
            return list
#    return list

print(quicksort([6,4,8,10,2,5]))
print(quicksort([10,8,6,5,4,2]))
print(quicksort([9,8,6,4,2]))