from hashlib import new
from tarfile import TarError


class LinkedNode():
    '''
    A node within a linked list
    
    Attributes
    ----------
    value : Any
        The value of the current node
        
    next : listNode | None
        The next node in the list, or None if current node is the tail
    '''
    
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    '''
    A list of linked nodes.
    
    Attributes
    ----------
    head : listNode | None
        First node in list. None if list empty
        
    tail : listNode | None
        Last node in the list. None if list is empty
        
    
    Methods
    --------
    append(self, value)
    
    prepend(self, value)
    
    insert_after(self, target, new_value)
    
    remove(self, value)
    
    __str__(self)
    '''
    
    def __init__(self):
        self.head = None #First node
        self.tail = None #Last node
        
    def append(self, new_node: LinkedNode):
        '''
        Append a new value after the tail
        '''
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def prepend(self, new_node: LinkedNode):
        '''
        Prepend a new value in the first position (head)
        '''
        
        # List empty
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        
        # List not empty
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insert_after(self, target_node: LinkedNode, new_node: LinkedNode):
        '''
        Insert a node after the target value. Inserts no node if 
        target not found.
        '''
        
        if target_node == None:
            self.prepend(new_node)
            
        elif target_node is self.tail:
            self.append(new_node)
            
        else:
            new_node.next = target_node.next
            target_node.next = new_node
    
    def remove_after(self, target_node: LinkedNode):
        '''
        Remove the target value
        '''
        if self.head == None:
            return
        
        if target_node == None:
            removed_node = self.head
            self.head = self.head.next
        
        elif target_node is self.tail:
            return None
            
        elif target_node.next is self.tail:
            removed_node = target_node.next
            target_node.next = target_node.next.next
            self.tail = target_node.next
        
        else:
            removed_node = target_node.next
            target_node.next = target_node.next.next
            
        removed_node.next = None
        return removed_node
    
    def __str__(self):
        '''
        Print the linked list in traditional python list format
        '''
        if self.head == None:
            return str([])
        
        current_node = self.head
        node_values = [current_node.value]
        
        while current_node.next != None:
            current_node = current_node.next
            node_values.append(current_node.value)
            
        return str(node_values)


if __name__ == '__main__':
    
    nodeA = LinkedNode(1)
    nodeB = LinkedNode(2)
    nodeC = LinkedNode(3)
    
    myList = LinkedList()
    myList.append(nodeA)
    myList.append(nodeB)
    myList.insert_after(None, nodeC)
    print(myList.remove_after(nodeC))
    
    
    print(myList)
    print(myList.head.value)
    print(myList.tail.value)
    