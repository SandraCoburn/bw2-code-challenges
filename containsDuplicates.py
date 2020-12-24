'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
#Naive Solution
'''
#loop through the array
#if index is the same continue
#put the duplicates into another array
#compare the duplicates to array and return true or false if condition met
 duplicates = []
     duplicates = []
    for i, num in enumerate(nums):
        for i2, num2 in enumerate(nums):
            if i == i2:
                continue
            if num == num2:
                duplicates.append(num)
    if num in duplicates:
        return True
    else:
        return False
'''
'''
  #sorting the array
    #using count to check how many times an element appears
    #sorted_array = sorted(set(nums), key=lambda ele:nums.count(ele))
   sorted_arr = sorted(nums)
   for num in range(len(sorted_arr)):

       if nums[num] == nums[num+1]:
           return True
       else:
            return False
'''
#one line solution:
# return True if len(set(nums)) < len(nums) else False

def containsDuplicate(nums):
    #hash table
    #loop through array and select duplicates to be added to hash table and compare
    h = {}
    for num in nums:
        if num in h:
            return True
        else: 
            h[num] = 1
    return False
   

arr1 = [1,2,3,1]
arr2 = [1,2,3,4]
arr3 = [1,1,1,3,3,4,3,2,4,2]
arr4 = [2,14,18,22,22]

print(containsDuplicate(arr2))
