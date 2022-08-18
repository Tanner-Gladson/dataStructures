from ctypes.wintypes import tagMSG
from turtle import left


class BinaryTreeNode():
    
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.leftChild = None
        self.rightChild = None
        
        
class BinarySearchTree():
    '''
    Attributes
    ----------
    root : BinaryTreeNode | None
    
    Methods
    -------
    search(self, value: int) -> BinaryTreeNode:
    
    remove(self, targetNode: BinaryTreeNode) -> Bool:
    
    add(self, targetNode: BinaryTreeNode) -> Bool:
    '''
    
    def __init__(self):
        self.root = None
        
    def __str__(self) -> str:
        
        outString = []
        
        def printFromNode(node: BinaryTreeNode):
            
            if node == None:
                return
            else:
                printFromNode(node.leftChild)
                outString.append(node.value)
                printFromNode(node.rightChild)
                
        printFromNode(self.root)
        
        return str(outString)
        
    def search(self, targetValue: int) -> BinaryTreeNode:
        '''
        Search the binary tree and return the node with target value
        '''
        
        if self.root == None:
            return None
            
        currNode = self.root
        
        while currNode != None:
            
            if currNode.value == targetValue:
                break
            
            elif targetValue > currNode.value:
                currNode = currNode.rightChild
                
            else:
                currNode = currNode.leftChild
        
        return currNode
    
    def removeNode(self, targetNode: BinaryTreeNode) -> bool:
        '''
        Remove a node from the tree
        '''
        # If target has no children
        if targetNode.leftChild == None and targetNode.rightChild == None:
            if targetNode is self.root:
                self.root = None
            else:
                parentNode = targetNode.parent
                if targetNode is parentNode.leftChild:
                    parentNode.leftChild = None
                else:
                    parentNode.rightChild = None
                    
        # Exclusively one child
        elif targetNode.rightChild == None or targetNode.leftChild == None:
            
            if targetNode.rightChild == None:
                successor = targetNode.leftChild
            else:
                successor = targetNode.rightChild
            
            
            if targetNode is self.root:
                self.root = successor
            else:
                predecessor = targetNode.parent
                if targetNode is predecessor.leftChild:
                    predecessor.leftChild = successor
                else:
                    predecessor.rightChild = successor
                
                successor.parent = predecessor
        
        # Two children:
        else:
            # Find successor
            successor = targetNode.rightChild
            while successor.leftChild != None:
                successor = successor.leftChild
            
            # Swap successor and targetNode
            targetNode.value = successor.value
            
            self.removeNode(successor)
            

    def insertNode(self, insertNode: BinaryTreeNode) -> bool:
        '''
        Add a node to the binary search tree.
        '''
        
        if self.root == None:
            self.root = insertNode
            return True
            
        currNode = self.root
        while currNode != None:
            
            if insertNode.value < currNode.value:
                if currNode.leftChild == None:
                    currNode.leftChild = insertNode
                    insertNode.parent = currNode
                    break
                else:
                    currNode = currNode.leftChild
                    
            elif insertNode.value >= currNode.value:
                if currNode.rightChild == None:
                    currNode.rightChild = insertNode
                    insertNode.parent = currNode
                    break
                else:
                    currNode = currNode.rightChild
                    
        return True
        
        
    def getHeight(self):
        
        def find_height(node: BinaryTreeNode):
            
            if node == None:
                return -1
            else:
                left_heigh = find_height(node.leftChild)
                right_height = find_height(node.rightChild)
                return 1 + max(left_heigh, right_height)
        
        return find_height(self.root)
    

if __name__ == '__main__':
    myTree = BinarySearchTree()
    
    nodeA = BinaryTreeNode(10)
    nodeB = BinaryTreeNode(15)
    nodeC = BinaryTreeNode(5)
    nodeD = BinaryTreeNode(12)
    nodeE = BinaryTreeNode(11)
    
    myTree.insertNode(nodeA)
    myTree.insertNode(nodeB)
    myTree.insertNode(nodeC)
    myTree.insertNode(nodeD)
    myTree.insertNode(nodeE)
    
    print(myTree.getHeight())