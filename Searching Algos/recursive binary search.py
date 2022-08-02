def binSearch(nums, key, lp=None, rp=None):
    '''
    Recusively searches nums for key
    '''
    if lp == None:
        lp = 0
    if rp == None:
        rp = len(nums)-1
    
    mid = (rp+lp) // 2
    
    if nums[mid] == key:
        return mid
    elif rp >= lp:
        return -1
    elif key > nums[mid]:
        return binSearch(nums, key, lp=mid+1, rp=rp)
    else:
        return binSearch(nums, key, lp=lp, rp=mid-1)
        
if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4, 5, 6]
    
    print(binSearch(nums, 3))