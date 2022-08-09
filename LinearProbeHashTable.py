class LinearProbeHashTable():
    '''
    A hashtable which will search linearly for earliest open bucket
    
    Attributes
    ----------
    size : int
        The size of the hashTable's array
        
    hashArray : list[int]
        The container of hashtable elements. An element of '-item' means
        empty after removal of 'item'
        
    Methods
    --------
    __str__(self):
    
    find_index(self, item: int):
        Find a) the first open index, or b) the index containing the item
        
    insert(self, item: int):
    remove(self, item: int):
    search(self, item: int):
    '''
    
    def __init__(self, size):
        self.size = size
        self.hashArray = [None for x in range(0, self.size)]
    
    def __str__(self):
        return str(self.hashArray)
    
    def find_index(self, item: int) -> int:
        '''
        Find an index for an item
        '''
        # Hash the item, and then find first empty bucket. 
        # If no buckets available, return None
        indx = item % self.size
        for i in range(self.size):
            wrapped_index = (indx + i) % self.size
            
            bucket = self.hashArray[wrapped_index]
            if bucket == item or bucket == None or bucket < 0:
                return wrapped_index
        
        return None
        
    def insert(self, item: int):
        '''Insert the item into hashtable'''
        
        index = self.find_index(item)
        if index == None:
            return
        else:
            self.hashArray[index] = item
    
    def remove(self, item: int):
        '''Remove item from a bucket if it exists. Replace element with 1'''
        index = self.find_index(item)
        
        if self.hashArray[index] == item:
            self.hashArray[index] = -item
        
    
    def search(self, item: int):
        index = self.find_index(item)
        
        if self.hashArray[index] == item:
            return self.hashArray[index]
    

if __name__ == '__main__':
    myHashTable = LinearProbeHashTable(10)
    
    myHashTable.insert(0)
    myHashTable.insert(100)
    myHashTable.insert(1)
    myHashTable.insert(9)
    myHashTable.insert(89)
    myHashTable.remove(89)
    myHashTable.insert(89)
    
    
    print(myHashTable)
    print(myHashTable.search(250))