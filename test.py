class Node:
    def __init__(self, data = None, left = None, right = None):
        self.val = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data, currentNode = None):
        newNode = Node(data)
        if currentNode is None:
            currentNode = self.root

        if self.root is None:
            self.root = newNode
            print(data, "inserted as root")
            return True
        elif currentNode.val == data:
            print(data, "inserted")
            return False
        elif currentNode.val > data:
            if currentNode.left:
                self.insert(data, currentNode.left)
            else:
                currentNode.left = newNode
                print(data, "inserted")
                return True
        elif currentNode.val < data:
            if currentNode.right:
                self.insert(data, currentNode.right)
            else:
                currentNode.right = newNode
                print(data, "inserted")
                return True


    def inorder(self, currentNode = None):
        if currentNode is None:
            currentNode = self.root
        
        if currentNode.left:
            self.inorder(currentNode.left)
        
        print(currentNode.val)
        
        if currentNode.right:
            self.inorder(currentNode.right)

myBST = BST()
myBST.insert(10)
myBST.insert(20)
myBST.insert(5)
myBST.insert(25)
myBST.inorder()
myBST.insert(12)
myBST.inorder()
myBST.insert(30)
myBST.insert(35)
myBST.insert(40)
myBST.insert(45)
myBST.insert(50)
myBST.insert(55)
myBST.inorder()