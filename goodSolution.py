def get_greatest_difference(nums):
  sorted_nums = sorted(nums)
  return sorted_nums[-1] - sorted_nums[0]

'''
Our runtime is now O(n * log2(n)).

This is because, while we didn't use any loops, the sort method uses O(n * log2(n)) time to run. We don't count
the last line of code in our equation because it is that fast.
'''
