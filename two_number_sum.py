# Time O(N2), Space O(1)
def twoNumberSum(array, targetSum):
    for i in range(len(array) -1):
        for j in range(i+1,len(array)):
            firstNum = array[i]
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []

# Time O(N), Space O(N)
def twoNumberSum_(array, targetSum):
    dict = {}
    for i in array:
        firstNum = i
        secondNum = targetSum - firstNum
        if secondNum in dict.keys():
            return [firstNum, secondNum]
        else:
            dict[i] = True
    return []

# Time O(NlogN), Space O(1)
def twoNumberSum__(array, targetSum):
    array.sort()
    left = 0
    right = len(array) -1
    while left < right:
        potentialSum = array[left] + array[right]
        if potentialSum == targetSum:
            return [array[left], array[right]]
        elif potentialSum > targetSum:
            right -= 1
        elif potentialSum < targetSum:
            left += 1
    return []
