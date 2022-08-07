
from linkedlist import LinkedNode, LinkedList

class doubleLinkedNode(LinkedNode):
    
    def __init__(self, value, previous_node, next_node):
        LinkedNode.__init__(self, value=value, next_node=next_node)
        self.previous = previous_node
        

class doubleLinkedList(LinkedList):
    '''
    Structure for double linked list
    
    Attributes
    ----------
    head : doubleLinkedNode | None
        First node, none if doesn't exist
    tail : doubleLinkedNode | None
        Second node, none if len = 0
        
        
    Methods
    --------
    append(self, value):
    
    prepend(self, value):
    
    insertAfter(self, target_value, new_value):
        Insert node with value = new_value after the first node
        with value = target value
        
    remove(self, value)
    
    print(self)
    '''
    def __init__(self):
        LinkedList.__init__(self)
        
    def append(self, value):
        
        if self.head == None:
            self.head = doubleLinkedNode(value, None, None)
            self.tail = self.head
        else:
            new_node = doubleLinkedNode(value, self.tail, None)
            self.tail.next = new_node
            self.tail = new_node
    
    def prepend(self, value):
        if self.head == None:
            self.head = doubleLinkedNode(value, None, None)
            self.tail = self.head
        else:
            new_node = doubleLinkedNode(value, None, self.head)
            self.head.previous = new_node
            self.head = new_node
    
    def insert_value_after(self, target_value, new_value):
        '''
        Insert node with value = new_value after the first node
        with value = target value
        '''
        if self.head == None:
            self.head = doubleLinkedNode(new_value, None, None)
            self.tail = self.head
            return
        
        
        current_node = self.head
        
        while current_node != None:
            
            if current_node.value == target_value:
                new_node = doubleLinkedNode(new_value, current_node, current_node.next)
                current_node.next = new_node
                
                # If current node was not tail, set successor node's rear
                # pointer to our new node. If it was the tail, change tail
                # to new node
                if current_node is self.tail:
                    self.tail = new_node
                else:
                    new_node.next.previous = new_node
                    
                break
            
            else:
                current_node = current_node.next
                
        
    def remove_after(self, target_value):
        
        if self.head == None:
            return
            
        current_node = self.head
        
        while current_node != None:
            
            if current_node.value != target_value:
                current_node = current_node.next
                continue
            
            # Cannot remove value after tail
            elif current_node is self.tail:
                return
                
            else:
                removed_node = current_node.next
                
                # If no successor
                if removed_node is self.tail:
                    self.tail = current_node
                    current_node.next = None
                
                # Else, if there is a successor, attach current node to succ.
                else:
                    successor_node = current_node.next.next
                    successor_node.previous = current_node
                    current_node.next = successor_node
                    print(myList.tail.value)
                
                # Detach removed node
                removed_node.next = None
                removed_node.previous = None
                break
    
    def remove_node(self, current_node: doubleLinkedNode):
        '''
        removes a node from doubly linked list
        '''
        predNode = current_node.previous
        succNode = current_node.next
        
        if current_node is self.head and current_node is self.tail:
            self.head = None
            self.tail = None
        
        elif current_node is self.head:
            self.head = succNode
            succNode.previous = None
        
        elif current_node is self.tail:
            self.tail = predNode
            predNode.next = None
        
        else:
            predNode.next = succNode
            succNode.previous = predNode
    
    
    def insert_node_after(self, target_node, inserted_node):
        '''
        Insert a node after a target node. If target node is None,
        insert at head of list
        '''
        
        if target_node == None:
            # Insert at head
            
            self.head.previous = inserted_node
            inserted_node.next = self.head
            
            self.head = inserted_node
            
        elif target_node is self.tail:
            # Insert after tail
            target_node.next = inserted_node
            inserted_node.previous = target_node
            
            self.tail = inserted_node
        
        else:
            succ_node = target_node.next
            inserted_node.next = target_node.next
            succ_node.previous = inserted_node
            inserted_node.previous = target_node
            target_node.next = inserted_node
        return
        
            
    def sort(self):
        '''
        Use insertion sort on the linked list
        '''
        
        # set first search & current_nodes
        search_node = self.head.next
        
        while search_node != None:
            current_node = search_node
            succNode = current_node.previous
            search_node = search_node.next
            
            self.remove_node(current_node)
            
            while succNode.value > current_node.value:
                succNode = succNode.previous
                if succNode == None:
                    break
                
            self.insert_node_after(succNode, current_node)
        
            
            
            
            
            
        
        

if __name__ =='__main__':
    myList = doubleLinkedList()
    myList.append(5)
    myList.append(2)
    myList.append(3)
    myList.append(4)
    myList.sort()
    
    print(myList)