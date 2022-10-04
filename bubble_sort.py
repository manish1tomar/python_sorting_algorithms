def bubble_sort(list):
    sorted = False
    for i in range(len(list)):
        if sorted == False:
            sorted = True
            for j in range(i+1,len(list),1):
                if list[i] > list[j]:
                    list[i], list[j] = list[j], list[i]
                    sorted = False
    return list

print(bubble_sort([5,6,3,8,7,5,1,2,3]))
print(bubble_sort([1,2,3,4,5]))