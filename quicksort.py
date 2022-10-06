def quicksort(list):
    low = 1
    high = len(list) -1
    while True:
        if low <= high:
            if list[low] > list[0]:
                if list[high] < list[0]:
                    list[low], list[high] = list[high], list[low]
                else:
                    high -= 1
            else:
                low +=1
        else:
            list[0], list[high] = list[high], list[0]
            if len(list[:high]) > 1:
                list[:high] = quicksort(list[:high])
            if len(list[high+1:]) > 1:
                list[high+1:] = quicksort(list[high+1:])
            return list

print(quicksort([6,4,8,10,2,5]))
print(quicksort([10,8,6,5,4,2]))
print(quicksort([9,8,6,4,2]))
print(quicksort([2,4,8,1,3,5,7,9,8]))