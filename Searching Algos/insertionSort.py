def insertionSort(nums):
    count = 0
    for rp in range(1, len(nums)):
        lp = rp
        while nums[lp-1] > nums[lp]:
            if lp == 0: break
            temp = nums[lp]
            nums[lp] = nums[lp-1]
            nums[lp-1] = temp
            count +=1
            lp -=1
            
    print(count)
            

if __name__ == '__main__':
    nums = [10, 24, 18, 19, 28, 31, 98, 75, 63]
    
    insertionSort(nums)
    
    print(nums)