def findClosestValueInBst(tree, target):
    diff = 9999999
    result = 9999999
    currentNode = tree
    
    while currentNode is not None:
        if diff > abs(target - currentNode.value):
                diff = abs(target - currentNode.value)
                result = currentNode.value
        
        if currentNode.value == target:
            return target
        elif currentNode.value > target:
            currentNode = currentNode.left
        elif currentNode.value < target:
            currentNode = currentNode.right
        else:
            return result
            break
    return result


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
