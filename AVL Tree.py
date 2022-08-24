from multiprocessing.sharedctypes import Value
from shutil import which


class AVLNode():
    
    def __init__(self, value):
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0
        self.balanceFactor = None
        self.value = value
        

class AVLTree():
    '''
    Attributes
    -----------
    root
    
    Methods
    ---------
    insertNode
    search
    removeNode
    
    
    '''
    def __init__(self):
        self.root = None
        
    def __str__(self) -> str:
        
        outString = []
        
        def printFromNode(node: AVLNode):
            
            if node == None:
                return
            else:
                printFromNode(node.left)
                outString.append(node.value)
                printFromNode(node.right)
                
        printFromNode(self.root)
        
        return str(outString)
        
    def search(self, targetValue: int) -> AVLNode:
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
                currNode = currNode.right
                
            else:
                currNode = currNode.left
        
        return currNode
    
    def removeNode(self, targetNode: AVLNode) -> bool:
        '''
        Remove a node from the tree
        '''
        # If target has no children
        parentNode = targetNode.parent
        
        if targetNode.left == None and targetNode.right == None:
            if targetNode is self.root:
                self.root = None
            else:
                parentNode = targetNode.parent
                if targetNode is parentNode.left:
                    parentNode.left = None
                else:
                    parentNode.right = None
                    
        # Exclusively one child
        elif targetNode.right == None or targetNode.left == None:
            
            if targetNode.right == None:
                successor = targetNode.left
            else:
                successor = targetNode.right
            
            
            if targetNode is self.root:
                self.root = successor
            else:
                predecessor = targetNode.parent
                if targetNode is predecessor.left:
                    predecessor.left = successor
                else:
                    predecessor.right = successor
                
                successor.parent = predecessor
        
        # Two children:
        else:
            # Find successor
            successor = targetNode.right
            while successor.left != None:
                successor = successor.left
            
            # Swap successor and targetNode
            targetNode.value = successor.value
            
            self.removeNode(successor)     
            
        while parentNode != None:
            self.rebalance(parentNode)
            parentNode = parentNode.parent

    def insertNode(self, newChild: AVLNode) -> bool:
        '''
        Add a node to the binary search tree.
        '''
        
        if self.root == None:
            self.root = newChild
            return True
            
        currNode = self.root
        while currNode != None:
            
            if newChild.value < currNode.value:
                if currNode.left == None:
                    currNode.left = newChild
                    newChild.parent = currNode
                    break
                else:
                    currNode = currNode.left
                    
            elif newChild.value >= currNode.value:
                if currNode.right == None:
                    currNode.right = newChild
                    newChild.parent = currNode
                    break
                else:
                    currNode = currNode.right
        
        # Rotate if necessary
        self.updateHeight(newChild)
        parentNode = newChild.parent
        
        while parentNode != None:
            self.rebalance(parentNode)
            parentNode = parentNode.parent
        
        return True 
    
    
    def updateHeight(self, node: AVLNode):
        ''' Update and get the height of a node. Precondition accurate child heights '''
        leftHeight = -1
        if node.left != None:
            leftHeight = node.left.height
        
        rightHeight = -1
        if node.right != None:
            rightHeight = node.right.height
            
        node.height = max(rightHeight, leftHeight) + 1
        return node.height
        
    def getBalance(self, node: AVLNode):
        ''' 
        Get the balance of a node 
        precondition of accurate children heights
        '''
        leftHeight = -1
        if node.left != None:
            leftHeight = node.left.height
        
        rightHeight = -1
        if node.right != None:
            rightHeight = node.right.height
            
        node.height = leftHeight - rightHeight

    def AVLTreeSetChild(self, parent: AVLNode, whichChild: str, newChild: AVLNode) -> bool:
        ''' Set a node as a child of another '''
        
        if whichChild == "right":
            parent.right = newChild
        elif whichChild == "left":
            parent.left = newChild
        
        if newChild != None:
            newChild.parent = parent
            
        self.updateHeight(parent)
        return True

    def AVLReplaceChild(self, parent: AVLNode, currChild: str, newChild: AVLNode) -> bool:
        ''' Replace one child node with a new node '''
        
        if parent.left is currChild:
            self.AVLTreeSetChild(parent, "left", newChild)
        elif parent.right is currChild:
            self.AVLTreeSetChild(parent, "right", newChild)
        return True
        
    def AVLGetBalance(self, node: AVLNode):
        self.updateHeight(node)
        return self.AVLGetBalance(node)
    
    def rightRotation(self, node: AVLNode):
        ''' Perform a right rotation at node '''
        leftRightChild = node.left.right
        
        if node is self.root:
            node.left.parent = None
            self.root = node.left
        else:
            self.AVLReplaceChild(node.parent, node, node.left)   
        
        self.AVLTreeSetChild(parent=node.left, whichChild="right", newChild=node)
        self.AVLTreeSetChild(parent=node, whichChild="left", newChild=leftRightChild)      
        
    def leftRotation(self, node: AVLNode):
        ''' Rotate left at node '''
        
        rightLeftChild = node.right.left
        
        if node.parent == None:
            self.root = node.right
            self.root.parent = None
        else:
            self.AVLReplaceChild(parent=node.parent, currChild=node, newChild=node.right)
            
        self.AVLTreeSetChild(parent=node.right, whichChild="left", newChild=node)
        self.AVLTreeSetChild(node, "right", rightLeftChild)
        
        
    def rebalance(self, node: AVLNode):
        ''' rebalance a subtree at node (after an insertion/removal) '''
        
        self.updateHeight(node)
        self.getBalance(node)
        
        if self.getBalance(node) == 2:
            if self.getBalance(node.left) == -1:
                # Double rotation
                self.leftRotation(node.left)
            self.rightRotation(node)
            
        elif self.getBalance(node) == -2:
            if self.getBalance(node.right) == 1:
                # Double rotation
                self.rightRotation(node.left)
            self.leftRotation(node)
        
    
    


if __name__ == '__main__':
    myTree = AVLTree()
    
    nodeA = AVLNode(10)
    nodeB = AVLNode(9)
    nodeC = AVLNode(8)
    nodeD = AVLNode(12)
    nodeE = AVLNode(11)
    
    myTree.insertNode(nodeA)
    myTree.insertNode(nodeB)
    myTree.insertNode(nodeC)
    #myTree.insertNode(nodeD)
    #myTree.insertNode(nodeE)
    
    myTree.updateHeight(myTree.root)
    myTree.rightRotation(nodeA)
    print(myTree.AVLGetBalance(nodeA))