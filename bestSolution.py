def get_greatest_difference(nums):
  max = nums[0]
  min = nums[0]
  for num in nums:
    if num > max:
      max = num
    elif num < min:
      min = num
  return max - min

'''
This is the best solution because we only use 1 for loop and we don't use a utility method (ie. sorted()).
Since we only run the for loop for n times in the array, we have a runtime of O(n).

While we do check for 2 things, the beauty of Big O is that we get to throw out the constants.
'''
