from pstats import FunctionProfile
from sre_constants import SUCCESS


class setNode():
    '''
    Attributes
    ----------
    data : int
    parent : setNode?
    left : setNode?
    right : setNode?
    
    Methods
    --------
    getSuccessor(self) -> setNode:
        Find the left most leaf node in right-subtree
        
    replaceChild(self, oldChild, newChild) -> None:
        Replace two childrend
    
    count(self) -> ?
    
    '''
    
    def __init__(self, data: int, parent=None, left=None, right=None) -> None:
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        
        
    def getSuccessor(self) -> 'setNode':
        ''' Find the next node in the binary tree order '''
        if self.right == None:
            node = self
            while (node.parent != None) and (node is node.parent.right):
                node = node.parent
                
            return node.parent
            
        else:
            successor = self.right
            while successor.left != None:
                successor = successor.left
                
            return successor
            
            
    def count(self) -> int:
        ''' Count the number of nodes in a subtree '''
        
        leftCount = 0
        if self.left != None:
            leftCount = self.left.count()
        
        rightCount = 0
        if self.right != None:
            rightCount = self.right.count()
            
        return 1 + rightCount + leftCount
    
    def setChild(self, whichChild: str, newChild: 'setNode') -> None:
        if whichChild == "right":
            self.right = newChild
        elif whichChild == "left":
            self.left = newChild
        
        if newChild != None:
            newChild.parent = self
        
    
    def replaceChild(self, oldChild: 'setNode', newChild: 'setNode') -> None:
        
        if oldChild is self.right:
            self.setChild(whichChild="right", newChild=newChild)
        
        elif oldChild is self.left:
            self.setChild(whichChild="left", newChild=newChild)


class BSTIterator():
    '''
    Attributes
    -----------
    currNode : setNode
        The current node we're checking out
        
    Methods
    -------
    __next__(self) -> None
        Sets the currNode value to the next node in sorted order
    '''
    
    def __init__(self, startNode: setNode) -> None:
        self.currNode = startNode
        
    def __next__(self):
        
        if self.currNode == None:
            raise StopIteration
        else:
            result = self.currNode
            self.currNode = self.currNode.getSuccessor()
            return result

class BSTset():
    '''
    Attributes
    -----------
    root : setNode?
    getKey : function
        Convert node data into integer
    
    Methods
    --------
    add(self, itemData: int) -> None:
        Add a new item as a node. Function creates a setNode instance
        and inserts into the tree.
        
    search(self, itemData: int) -> setNode:
        Search the tree for a key and find it
        
    remove(self, itemData: int) -> None:
        Search for an item and remove if it exists
    
    __len__(self) -> int
    
    difference(self, other: 'BSTset') -> 'BSTset':
        Return the elements present in self that are not in other
    
    union(self, other: 'BSTset') -> 'BSTset':
        Return a new set of elements in both sets
    
    intersect(self, other: 'BSTset') -> 'BSTset'
        Return a new set of elements in both sets, but only if in both
    
    filter(self, filterFunc: function) -> 'BSTset':
        Create a new set from items in self if they pass the filter
        
    map(self, mapFunc: function) -> 'BSTset':
        Create a new set from items in self, applying the mapFunc argument
        
    '''
    
    def __init__(self, getKey=None) -> None:
        self.root = None
        
        if getKey != None:
            self.getKey = getKey
        else:
            self.getKey = lambda x: x
    
    
    def add(self, itemData: int) -> None:
        '''
        Add a new item as a node. Function creates a setNode instance
        and inserts into the tree.
        '''
        
        if itemData == None:
            return
        
        key = self.getKey(itemData)
        newNode = setNode(itemData)
        
        parent = self.root
        
        if parent == None:
            self.root = newNode
            return
        
        while True:
            
            if key == self.getKey(parent.data):
                break
            
            if key < self.getKey(parent.data):
                if parent.left == None:
                    parent.setChild("left", newNode)
                    break
                else:
                    parent = parent.left
            
            elif key > self.getKey(parent.data):
                if parent.right == None:
                    parent.setChild("right", newNode)
                    break
                else:
                    parent = parent.right
    
    def __str__(self):
        result = [node.data for node in self]
        return str(result)
        
        
    def search(self, itemData: int) -> setNode:
        ''' Search the tree for a key and find it '''
        key = self.getKey(itemData)
        node = self.root
        
        while node != None:
            if key == self.getKey(node.data):
                return node
            
            if key < self.getKey(node.data):
                node = node.left
            
            elif key > self.getKey(node.data):
                node = node.right
                
        return None
        
        
    def removeNode(self, node: setNode) -> None:
        ''' Search for an item and remove if it exists '''

        if node.right == None and node.left == None:
            if node is not self.root:
                node.parent.replaceChild(node, None)
            else:
                self.root = None
        
        elif node.right == None:
            if node is not self.root:
                node.parent.replaceChild(node, node.left)
            else:
                self.root = node.left
                self.root.parent = None
                
        elif node.left == None:
            if node is not self.root:
                node.parent.replaceChild(node, node.right)
            else:
                self.root = node.right
                self.root.parent = None
                
        else:
            successor = node.right
            while successor.left != None:
                successor = successor.left
                
            node.data = successor.data
            self.removeNode(successor)
                
    
    def removeValue(self, itemData: int) -> None:
        node = self.search(itemData)
        
        if node == None:
            return
        else:
            self.removeNode(node)
    
    
    def __contains__(self, itemData: int) -> bool:
        ''' Bool if the set contains that value'''
        if self.search(itemData) == None:
            return False
        else:
            return True
    
    
    def __iter__(self):
        ''' Return iterator class '''
        startNode = self.root
        while startNode != None and startNode.left != None:
            startNode = startNode.left
            
        return BSTIterator(startNode=startNode)
    
    
    def __len__(self) -> int:
        return self.root.count()
    
    
    def difference(self, other: 'BSTset') -> 'BSTset':
        ''' Return the elements present in self that are not in other '''
        result = BSTset()
        
        for node in self:
            if node.data not in other:
                result.add(node.data)
                
        return result
    
    
    def union(self, other: 'BSTset') -> 'BSTset':
        ''' Return a new set of elements in both sets '''
        
        newSet = BSTset()
        
        for node in self:
            newSet.add(node.data)
        
        for node in other:
            newSet.add(node.data)
            
        return newSet
        
      
    def intersect(self, other: 'BSTset') -> 'BSTset':
        ''' Return a new set containg common elements '''
        newSet = BSTset()
        
        for node in self:
            if node.data in other:
                newSet.add(node.data)
                
        return newSet
    
    
    def filter(self, filterFunc) -> 'BSTset':
        ''' Create a new set from items in self if they pass the filter '''
        newSet = BSTset()
        for node in self:
            if filterFunc(node.data) == True:
                newSet.add(node.data)
            
        return newSet
        
        
    def mapSet(self, mapFunc) -> 'BSTset':
        ''' Create a new set, applying the mapFunc argument to self's items '''
        newSet = BSTset()
        for node in self:
            newSet.add(mapFunc(node.data))
            
        return newSet

def multiply(input):
    return input * 2
    
def bigNum(input):
    if input > 4:
        return True
    else:
        return False

if __name__ == '__main__':
    set1 = BSTset()
    set1.add(5)
    set1.add(4)
    set1.add(7)
    
    set2 = BSTset()
    set2.add(5)
    set2.add(7)
    set2.add(10)
    
    result = set1.filter(bigNum)
    print(result)
        
    