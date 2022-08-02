def addNode(heap, new_val):
    '''
    Adds & percolates a new node into a maxheap
    '''
    
    # Append new node
    heap.append(new_val)
    
    child_indx = len(heap) - 1
    parent_indx = (child_indx-1)//2
    
    # Continously percolate upwards until parent > node
    while heap[child_indx] > heap[parent_indx] and parent_indx >= 0:
        print(parent_indx)
        temp = heap[child_indx]
        heap[child_indx] = heap[parent_indx]
        heap[parent_indx] = temp
        
        child_indx = parent_indx
        parent_indx = (parent_indx-1)//2
        
        
def popMax(heap):
    '''
    Pop the max node of a heap
    '''
    
    # place last in first, pop last
    heap[0] = heap[-1]
    heap.pop(-1)
    pointer = 0
    
    # percolate downwards
    while True:
        print(pointer)
        
        if pointer*2 + 1 >= len(heap):
            break
                
        if pointer*2 + 2 >= len(heap):
            if heap[pointer*2+1] > heap[pointer]:
                
                temp = heap[pointer*2+1]
                heap[pointer*2+1] = heap[pointer]
                heap[pointer] = temp
                pointer = pointer*2 + 1
                
        else:
            maxValue = max(heap[pointer*2+1], heap[pointer*2+2], heap[pointer])
            
            if heap[pointer*2+1] == maxValue:
                temp = heap[pointer*2+1]
                heap[pointer*2+1] = heap[pointer]
                heap[pointer] = temp
                pointer = pointer*2 + 1
                
            elif heap[pointer*2+2] == maxValue:
                temp = heap[pointer*2+2]
                heap[pointer*2+2] = heap[pointer]
                heap[pointer] = temp
                pointer = pointer*2 + 2
                
            elif heap[pointer] == maxValue:
                break
    
if __name__ == '__main__':
    heap = [8,7,6,5,4,3]
    
    popMax(heap)
    
    print(heap)
        