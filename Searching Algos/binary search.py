from array import array
def binSearch(numbers: list[int], key: int) -> int:
    '''
    Finds the index of element 'key' in list. If key not in list, returns -1
    '''
    index = -1
    rp = len(numbers) - 1
    lp = 0

    while True:
        mid = (rp+lp) // 2
        print(mid)
        
        if numbers[mid] == key:
            index = mid
            break
            
        elif rp == lp:
            break
            
        elif numbers[mid] < key:
            lp = mid+1
            
        elif numbers[mid] > key:
            rp = mid-1
            
    return index
    
if __name__ == '__main__':
    nums = [1,2,3,4,5,6,8]
    print(binSearch(nums, 3))
    
    # Learn? Always start inequalities with your input, it makes
    # it more readbable imo