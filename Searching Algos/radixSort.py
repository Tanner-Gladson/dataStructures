def radix_bucketSort(nums, digit):
    '''
    Sort the values into buckets, and copy back into list
    '''
    buckets = [[], [], [], [], [], [], [], [], [], []]
    
    for i in range(0, len(nums)):
        val = (nums[i] % 10**(digit+1)) // (10**digit)
        
        buckets[val].append(nums[i])
    
    i = 0
    for bucket in buckets:
        for num in bucket:
            nums[i] = num
            i += 1
            

def radix_get_max_length(nums):
    '''Find the number of digits in largest value'''
    
    max_num = max(nums)
    
    return len(str(max_num))

def radixSort(nums):
    '''
    Sort a list of numbers in O(N)
    '''
    max_length = radix_get_max_length(nums)
    
    
    for digit_pos in range(0, max_length):
        radix_bucketSort(nums, digit_pos)

        

if __name__ == '__main__':
    nums = [3,68,4,3,44,6,7,688]
    
    radixSort(nums)
    
    print(nums)