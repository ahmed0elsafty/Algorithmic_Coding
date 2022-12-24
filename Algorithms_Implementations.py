from DataStructure import *

# Binary Search
def binary_search(arr:list, value):
    # O(log(n))
    arr.sort()
    size = len(arr)
    low, high = 0, size-1
    while low <= high:
        mid = (low + high) // 2
        if value == arr[mid]:
            return mid + 1 
        elif value > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

#Tree Traversals (Inorder, Preorder and Postorder)
class TreeTraversal:

    def inOrder(self, root: TreeNode):
        if root:
            self.inOrder(root.left)
            print(root.value)
            self.inOrder(root.right)
            
    def preOrder(self,root: TreeNode):
        if root:
            print(root.value)
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self, root: TreeNode):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.value)

