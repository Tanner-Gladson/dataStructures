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
        self.prepend(new_node)
        
    def pop(self) -> LinkedNode:
        return self.remove_after(None)
        
if __name__ == "__main__":
    myStack = Stack()
    
    nodeA = LinkedNode(1)
    nodeB = LinkedNode(2)
    nodeC = LinkedNode(3)
    
    myStack.push(nodeA)
    myStack.pop()
    
    print(myStack)