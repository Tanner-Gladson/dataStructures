from tempfile import tempdir


def partitition(nums, lp, rp):
    
    pivot = nums[(lp +rp) // 2]
    print(pivot)
    done = False
    
    while not done:
        print(nums)
        print('rp:', rp)
        print('lp:', lp)
        while nums[lp] < pivot:
            lp += 1
            
        while nums[rp] > pivot:
            rp -= 1
            
        if lp >= rp:
            break
            
        else:
            temp = nums[rp]
            nums[rp] = nums[lp]
            nums[lp] = temp
            rp -= 1
            lp += 1
            
    return rp
            

def quickSort(nums, lp, rp):
    
    if lp >= rp:
        return
    
    pivot_indx = partitition(nums, lp, rp)
    
    quickSort(nums, lp, pivot_indx)
    
    quickSort(nums, pivot_indx+1, rp)


if __name__ == '__main__':
    nums = [5,1,9,8,5,6,7,1,5,3]
    
    quickSort(nums, 0, len(nums)-1)
    
    print(nums)
    