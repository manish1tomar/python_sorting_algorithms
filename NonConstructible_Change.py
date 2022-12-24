# Time Complexity O(N LogN)
# Space Complexity O(1) because of in place sorting
def nonConstructibleChange(coins):
    change = 0
    coins.sort()
    for i in coins:
        if i > change +1:
            return change +1
        change += i
        
    return change +1
