def merge(nums, lp, rp):
    '''
    Sort a subsection of nums
    '''
    
    mid = (lp+rp) // 2
    last_left = lp
    last_right = mid+1
    i = 0
    buffer = [None] * (rp-lp+1)
    
    while last_left <= mid and last_right <= rp:
        if nums[last_left] > nums[last_right]:
            buffer[i] = nums[last_right]
            last_right += 1
        else:
            buffer[i] = nums[last_left]
            last_left += 1
        i += 1
        
    while last_left <= mid:
        buffer[i] = nums[last_left]
        last_left += 1
        i +=1
    
    while last_right <= rp:
        buffer[i] = nums[last_right]
        last_right += 1
        i +=1
    
    i = lp
    for num in buffer:
        nums[i] = num
        i += 1

def mergeSort(nums, lp, rp):
    if lp == rp:
        return
    
    mid = (lp+rp) // 2
    
    mergeSort(nums, lp, mid)
    mergeSort(nums, mid+1, rp)
    merge(nums, lp, rp)
            
            
if __name__ == '__main__':
    nums= [5,7,4,24,8,5,6,7,3,4,5,67,8]
    
    mergeSort(nums, 0, len(nums)-1)
    
    print(nums)
            
            