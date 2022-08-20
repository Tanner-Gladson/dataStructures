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
        
        