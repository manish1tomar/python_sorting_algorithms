# Space Complexity O(N)
# Time Complexity O(N)

def branchSum(node, runningSum, arr):
    if node is not None:
        runningSum += node.value
        branchSum(node.left, runningSum, arr)
        branchSum(node.right, runningSum, arr)
        if node.left is None and node.right is None:
            arr.append(runningSum)
    
def branchSums(root):
    arr = []
    branchSum(root, 0, arr)
    return arr
