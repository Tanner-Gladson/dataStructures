class RBNode():
    '''
    Attributes
    -----------
    left : rbNode?
    right : rbNode?
    parent : rbNode?
    height : int
    
    Methods
    --------
    updateHeight(self)
        Precondition of accurate child heights
        
    setChild(self, whichChild: str, newChild: rbNode) -> bool:
    replaceChild(self, oldChild: rbNode, newChild: rbNode) -> bool:
    '''
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.height = None
        self.color = None
        
    def updateHeight(self) -> None:
        ''' Precondition of accurate child heights '''
        leftHeight = -1
        if self.left != None:
            leftHeight = self.left.height
            
        rightHeight = -1
        if self.right != None:
            rightHeight = self.right.height
            
        return max(rightHeight, leftHeight) + 1
        
    def setChild(self, whichChild: str, newChild: 'RBNode') -> bool:
        ''' Overwrite a child '''
        
        if whichChild != "right" and whichChild != "left":
            return False
        
        if whichChild == "right":
            self.right = newChild
        else:
            self.left = newChild
            
        if newChild != None:
            newChild.parent = self
        
        return True
    
    def replaceChild(self, oldChild: 'RBNode', newChild: 'RBNode') -> bool:
        ''' Replace a childNode'''
        
        if oldChild is self.right:
            return self.setChild(whichChild="right", newChild=newChild)
        
        elif oldChild is self.left:
            return self.setChild(whichChild="left", newChild=newChild)
        
        else:
            return False
            


class RBTree():
    '''
    Attributes
    -----------
    root : RBNode?
    
    Methods
    ------------
    rightRotation(self, node) -> None:
    leftRotation(self, node) -> None:
    
    insertNode(self, newNode: RBNode) -> None
    removeNode(self, targetNode: RBNode) -> bool
    
    '''
    
    def rightRotation(self, node: RBNode) -> None:
        ''' Perform a right rotation at node '''
        if node.left == None:
            return None
        
        leftRightChild = node.left.right
         
        if node.parent == None:
            self.root = node.left
            self.root.parent = None
        else:
            node.parent.replaceChild(oldChild=node, newChild=node.left)
            
        node.left.setChild(whichChild="right", newChild = node)
        node.setChild("left", leftRightChild)
    
    
    def leftRotation(self, node: RBNode) -> None:
        
        if node.right == None:
            return
            
        rightLeftChild = node.right.left
        
        if node.parent == None:
            self.root = node.right
            self.root.parent = None
        else:
            node.parent.replaceChild(oldChild = node, newChild = node.right)
            
        node.right.setChild("left", node)
        node.setChild("right", rightLeftChild)
        
    def insertNode(self, newNode: RBNode) -> None:
        ''' Insert a node using BST rules, then balance '''
        
        if self.root == None:
            self.root = newNode
            return True
            
        currNode = self.root
        while currNode != None:
            
            if newNode.value < currNode.value:
                if currNode.leftChild == None:
                    currNode.leftChild = newNode
                    newNode.parent = currNode
                    break
                else:
                    currNode = currNode.leftChild
                    
            elif newNode.value >= currNode.value:
                if currNode.rightChild == None:
                    currNode.rightChild = newNode
                    newNode.parent = currNode
                    break
                else:
                    currNode = currNode.rightChild
        
        newNode.color = "red"
        
        self.balanceTree(newNode)
        
    def balanceTree(self, node: RBNode) -> None:
        ''' Rebalance a tree from node '''
        
        if node == self.root:
            node.color = "black"
            return
            
        parent = node.parent
        if parent.color == "black":
            return
            
        grandparent = parent.parent
        if grandparent == None:
            return
        
        if parent is grandparent.left:
            uncle = grandparent.right
        else:
            uncle = grandparent.left
        
        # If we have an uncle node, propogate color changes
        if uncle != None and uncle.color == "red":
            parent.color = "black"
            uncle.color = "black"
            grandparent.color = "red"
            self.balanceTree(grandparent)
            return
        
        # Double rotation case
        if parent is grandparent.left and node is parent.right:
            self.leftRotation(parent)
            # Reset node & parent pointers
            node = parent
            parent = node.parent
        elif parent is grandparent.right and node is parent.left:
            self.rightRotation(parent)
            node = parent
            parent = node.parent
        
        # Single rotation to balance
        parent.color = "black"
        grandparent.color = "red"
        if node is parent.left:
            self.rightRotation(parent)
        else:
            self.leftRotation(parent)
        
        
        
        
        