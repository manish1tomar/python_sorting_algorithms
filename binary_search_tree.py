class Node:
    def __init__(self, data, leftChild = None, rightChild = None):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild
    
    def insert(self, data):
        if self.data == data:
            return False
        elif self.data > data:
            if self.leftChild is not None:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild is not None:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True
    
    def find(self, data):
        if self.data == data:
            return True
        elif self.data > data:
            if self.leftChild is not None:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild is not None:
                return self.rightChild.find(data)
            else:
                return False
    
    def preorder(self):
        if self:
            print(str(self.data))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.data))
            if self.rightChild:
                self.rightChild.inorder()

            
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return True
        else:
            return self.root.insert(data)
    
    def find(self, data):
        if self.root is None:
            return False
        else:
            return self.root.find(data)
    
    def preorder(self):
        print("Preorder:")
        self.root.preorder()

    def postorder(self):
        print("Postorder:")
        self.root.postorder()

    def inorder(self):
        print("Inorder:")
        print("Root is", self.root.__dict__)
        self.root.inorder()
    
    def remove(self, data):
        print("Removing", data, "Root is", self.root.__dict__)
        
        if self.root.leftChild is None and self.root.rightChild is None:
            self.root = None
        elif self.root.leftChild and self.root.rightChild is None:
            self.root = self.root.leftChild
        elif self.root.leftChild is None and self.root.rightChild:
            self.root = self.root.rightChild
        elif self.root.leftChild and self.root.rightChild:
            parent = None
            current_node = self.root
            while current_node and current_node.data != data:
                parent = current_node
                if current_node.data > data:
                    current_node = current_node.leftChild
                else:
                    current_node = current_node.rightChild
    
            if current_node is None or current_node.data != data:
                return False
            
            elif current_node.leftChild is None and current_node.rightChild is None:
                if data < parent.data:
                    parent.leftChild = None
                else:
                    parent.rightChild = None
                return True
            
            elif current_node.leftChild and current_node.rightChild is None:
                if data < parent.data:
                    parent.leftChild = current_node.leftChild
                else:
                    parent.rightChild = current_node.leftChild

            elif current_node.leftChild is None and current_node.rightChild:
                if data < parent.data:
                    parent.leftChild = current_node.rightChild
                else:
                    parent.rightChild = current_node.rightChild

            # Node has both left anf right child
            else:
                delNodeParent = node
                delNode = current_node.rightChild
                
                while delNode.leftChild:
                    delNodeParent = delNode
                    delNode = delNode.leftChild
                
                current_node.data = delNode.data
                if delNode.rightChild:
                    delNodeParent.leftChild = delNode.rightChild
                delNode = None

myBST = BinarySearchTree()
myBST.insert(10)
print(myBST.insert(15))
myBST.insert(20)
myBST.insert(5)
myBST.insert(25)
myBST.preorder()
myBST.postorder()
myBST.inorder()
myBST.insert(12)
myBST.inorder()
myBST.insert(30)
myBST.insert(35)
myBST.insert(40)
myBST.insert(45)
myBST.insert(50)
myBST.insert(55)
myBST.remove(5)
myBST.inorder()
