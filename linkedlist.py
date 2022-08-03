


from zmq import PLAIN_PASSWORD


class listNode():
    '''
    A node within a linked list
    
    Attributes
    ----------
    value : Any
        The value of the current node
        
    next : listNode | None
        The next node in the list, or None if current node is the tail
    '''
    
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node


class linkedList():
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
        
    def append(self, value):
        '''
        Append a new value after the tail
        '''
        if self.head == None:
            self.head = listNode(value, next_node=None)
            self.tail = self.head
            
        else:
            new_node = listNode(value, next_node=None)
            self.tail.next = new_node
            self.tail = new_node
    
    def prepend(self, value):
        '''
        Prepend a new value in the first position (head)
        '''
        
        # List empty
        if self.head == None:
            self.head = listNode(value, next_node=None)
            self.tail = self.head
        
        # List not empty
        else:
            new_node = listNode(value, next_node=self.head)
            self.head = new_node
    
    def insert_after(self, target, new_value):
        '''
        Insert a node after the target value. Inserts no node if 
        target not found.
        '''
        current_node = self.head
        
        while current_node != None:
            if current_node.value == target:
                new_node = listNode(new_value, next_node=current_node.next)
                current_node.next = new_node
                
                return
            
            else:
                current_node = current_node.next
    
    def remove(self, target_value):
        '''
        Remove the target value
        '''
        if self.head == None:
            return
        
        if self.head.value == target_value:
            if self.head is self.tail:
                self.head = None
                self.tail = None
                return
            
            else:
                removed_node = self.head
                self.head = removed_node.next
                removed_node.next = None
                removed_node.value = None
                return
        
        current_node = self.head
        
        while current_node.next != None:
            next_node = current_node.next
            
            if next_node.value == target_value:
                current_node.next = next_node.next
                next_node.next = None
                next_node.value = None
                
            else:
                current_node = next_node
    
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
    myList = linkedList()
    myList.append(1)
    myList.append(3)
    myList.remove(1)
    
    print(myList)
    