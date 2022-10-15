class MaxHeap:
    def __init__(self, list = []):
        self.Heap = list
    
    def __swap(self, idx1, idx2):
        self.Heap[idx1], self.Heap[idx2] = self.Heap[idx2], self.Heap[idx1]
    
    def __isLeaf(self, idx):
        if ( ( (idx + 1) * 2 ) - 1 ) > ( len(self.Heap) - 1 ):
            return True
        else:
            return False
    
    def __children(self, idx):
        rightChild = (idx + 1) * 2 
        leftChild = rightChild - 1
        return leftChild, rightChild
    
    def __bottomDown(self, idx):
        left_child_idx, right_child_idx = self.__children(idx)
        if self.__isLeaf(idx) is False:
            if right_child_idx < len(self.Heap):
                if self.Heap[right_child_idx] > self.Heap[left_child_idx]:
                    if self.Heap[right_child_idx] > self.Heap[idx]:
                        self.__swap(right_child_idx, idx)
                        self.__bottomDown(right_child_idx)
                elif self.Heap[left_child_idx] > self.Heap[idx]:
                    self.__swap(left_child_idx, idx)
                    self.__bottomDown(left_child_idx)
            else:
                if self.Heap[left_child_idx] > self.Heap[idx]:
                    self.__swap(left_child_idx, idx)
                    self.__bottomDown(left_child_idx)
    
    def heapify(self):
        for i in reversed(range(len(self.Heap))):
            self.__bottomDown(i)
    
    def heapSort(self):
        sorted_list = []
        while len(self.Heap) != 0:
            self.__swap(0, -1)
            sorted_list.append(self.Heap[-1])
            self.Heap.pop()
            self.__bottomDown(0)
        self.Heap = sorted_list
            
class MinHeap:
    def __init__(self, list = []):
        self.Heap = list
    
    def __swap(self, idx1, idx2):
        self.Heap[idx1], self.Heap[idx2] = self.Heap[idx2], self.Heap[idx1]
    
    def __isLeaf(self, idx):
        if ( ( (idx + 1) * 2 ) - 1 ) > ( len(self.Heap) - 1 ):
            return True
        else:
            return False
    
    def __children(self, idx):
        rightChild = (idx + 1) * 2 
        leftChild = rightChild - 1
        return leftChild, rightChild
    
    def __bottomDown(self, idx):
        left_child_idx, right_child_idx = self.__children(idx)
        if self.__isLeaf(idx) is False:
            if right_child_idx < len(self.Heap):
                if self.Heap[right_child_idx] < self.Heap[left_child_idx]:
                    if self.Heap[right_child_idx] < self.Heap[idx]:
                        self.__swap(right_child_idx, idx)
                        self.__bottomDown(right_child_idx)
                elif self.Heap[left_child_idx] < self.Heap[idx]:
                    self.__swap(left_child_idx, idx)
                    self.__bottomDown(left_child_idx)
            else:
                if self.Heap[left_child_idx] < self.Heap[idx]:
                    self.__swap(left_child_idx, idx)
                    self.__bottomDown(left_child_idx)
    
    def heapify(self):
        for i in reversed(range(len(self.Heap))):
            self.__bottomDown(i)
    
    def heapSort(self):
        sorted_list = []
        while len(self.Heap) != 0:
            self.__swap(0, -1)
            sorted_list.append(self.Heap[-1])
            self.Heap.pop()
            self.__bottomDown(0)
        self.Heap = sorted_list

'''myMaxHeap = MaxHeap([10,20,30,40,50])
print(myMaxHeap.Heap)
myMaxHeap.heapify()
print(myMaxHeap.Heap)
myMaxHeap.heapSort()
print(myMaxHeap.Heap)

myMaxHeap = MaxHeap([6,4,8,10,2,5])
myMaxHeap.heapify()
myMaxHeap.heapSort()
print(myMaxHeap.Heap)
myMaxHeap = MaxHeap([10,8,6,5,4,2])
myMaxHeap.heapify()
myMaxHeap.heapSort()
print(myMaxHeap.Heap)
myMaxHeap = MaxHeap([9,8,6,4,2])
myMaxHeap.heapify()
myMaxHeap.heapSort()
print(myMaxHeap.Heap)
myMaxHeap = MaxHeap([2,4,8,1,3,5,7,9,8])
myMaxHeap.heapify()
myMaxHeap.heapSort()
print(myMaxHeap.Heap)'''

myMinHeap = MinHeap([10,20,30,40,50])
myMinHeap.heapify()
myMinHeap.heapSort()
print(myMinHeap.Heap)

myMinHeap = MinHeap([6,4,8,10,2,5])
myMinHeap.heapify()
myMinHeap.heapSort()
print(myMinHeap.Heap)
myMinHeap = MinHeap([10,8,6,5,4,2])
myMinHeap.heapify()
myMinHeap.heapSort()
print(myMinHeap.Heap)
myMinHeap = MinHeap([9,8,6,4,2])
myMinHeap.heapify()
myMinHeap.heapSort()
print(myMinHeap.Heap)
myMinHeap = MinHeap([2,4,8,1,3,5,7,9,8])
myMinHeap.heapify()
myMinHeap.heapSort()
print(myMinHeap.Heap)
