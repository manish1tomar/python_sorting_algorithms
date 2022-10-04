def bubble_sort(list):
    for i in range(len(list)):
        for j in range(i+1,len(list),1):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

print(bubble_sort([5,6,3,8,7,5,1,2,3]))