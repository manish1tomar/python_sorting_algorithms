result_depth = 0

def nodeDepth(node, depth):
    global result_depth
    if node.left is None and node.right is None:
        pass
    else:
        depth += 1
        if node.left is not None:
            result_depth += depth
            nodeDepth(node.left, depth)
        if node.right is not None:
            result_depth += depth
            nodeDepth(node.right, depth)
        
def nodeDepths(root):
    global result_depth
    result_depth = 0
    depth = nodeDepth(root, 0)
    return result_depth
