'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
'''
#one solution:
'''
# initialize  array to hold indexes of matching numbers
## loop through the array and check for numbers that might meet the condition
 total = []
    for ind1, val1 in enumerate(nums):
        for ind2, val2 in enumerate(nums):
            if val1 + val2 == target and ind1 != ind2:
                total.append(ind1)
                print("total", val1, val2)
            
    return total
'''

def twoSum(nums, target):
    #initialize cache
    #loop through array with enumerate to get index
    #variable to hold the condition
    #Check that condition is in cache, return with index if it does
    #else, add to cache

    cache = {}
    for i, val in enumerate(nums):
        num = target - val
        if num in cache:
            return [cache[num], i]  
        else:
           cache[val] = i
                  
nums = [2,7,11,15]
nums2 = [3,2,4]
target = 9
print(twoSum(nums,9))
