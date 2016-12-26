def get_greatest_difference(nums):
  greatest_difference = 0
  for num1 in nums:
    for num2 in nums:
      difference = num1 - num2
      if difference > greatest_difference:
        greatest_difference = difference
  return greatest_difference

'''
This code gets the job done by finding every possible difference and comparing it with each other and finding the max.

While it gets the job done, it has a runtime of O(n²) because the outer loop runs n times and the inner loop runs for each time the outer loop is run (n * n).
'''
