from linkedlist import LinkedList, LinkedNode


from linkedlist import LinkedList

class Stack(LinkedList):
    '''
    LI FO
    Attributes
    -----------
    head : LinkedNode | None
    tail : LinkedNode | None
    
    Methods
    -------
    push(self, new_node: linkedList) -> None:
    pop(self) -> linkedNode
    peek(self) -> LinkedNode
    isEmpty(self) -> Bool
    '''
    
    def __init__(self):
        LinkedList.__init__(self)
    
    def push(self, new_node: LinkedNode) -> None:
        '''
        Add an element to the top of the stack
        '''
        self.prepend(new_node)
        
    def pop(self) -> LinkedNode:
        '''
        Remove & return the top element of the stack
        '''
        return self.remove_after(None)
    
    def peek(self):
        '''
        Return the top node in the stack
        '''
        if self.head == None:
            return None
        else:
            return self.head
            
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
    
        
if __name__ == "__main__":
    myStack = Stack()
    
    nodeA = LinkedNode(1)
    nodeB = LinkedNode(2)
    nodeC = LinkedNode(3)
    
    myStack.push(nodeA)
    
    print(myStack)
    print(myStack.peek().value)