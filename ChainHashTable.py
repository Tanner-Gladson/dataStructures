from linkedlist import LinkedList, LinkedNode


class ChainedHashTable():
    '''
    Contains a list of lists, which contain their respective objects
    
    Attributes
    -----------
    hashArray : list[LinkedList]
        Array of buckets
        
    size : int
        Length of hashArray
    
    
    Methods
    ---------
    hash(self, item)
    search(self, item)
    insert(self, item)
    remove(self, item)
    __str__(self)
    
    '''
    
    def __init__(self, size):
        self.size = size
        
        self.hashArray = [None for x in range(0, size)]
        
    
    def hash(self, item: int) -> int:
        '''
        hash the item to find its corresponding indx
        '''
        
        return item % self.size
        
        
    def search(self, item: int) -> LinkedList:
        '''
        Return the item corresponding to key 'item'
        '''
        
        return self.hashArray[self.hash(item)]
    
    
    def insert(self, item: int):
        '''
        Insert the item into its corresponding bucket. Create list or append
        '''
        newNode = LinkedNode(item)
        
        if self.search(item) == None:
            indx = self.hash(item)
            self.hashArray[indx] = LinkedList()
        
        self.search(item).append(newNode)
        
        
    def __str__(self):
        return str([str(x) for x in self.hashArray])
        


if __name__ == '__main__':
    my_table = ChainedHashTable(4)
    
    my_table.insert(2)
    my_table.insert(34)
    
    print(my_table)
    
    

