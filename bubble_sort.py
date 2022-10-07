def bubble_sort(list):
    sorted = False
    for i in range(len(list)):
        for j in range(i+1,len(list),1):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

print(bubble_sort([5,6,3,8,7,5,1,2,3]))
print(bubble_sort([5,4,3,2,1]))
print(bubble_sort([6,4,8,10,2,5]))
print(bubble_sort([10,8,6,5,4,2]))
print(bubble_sort([9,8,6,4,2]))
print(bubble_sort([2,4,8,1,3,5,7,9,8]))