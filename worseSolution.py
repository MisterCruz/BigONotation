def get_greatest_difference(nums):
  greatest_difference = 0
  for num1 in nums:
    for num2 in nums:
      difference = num1 - num2
      if difference > greatest_difference:
        greatest_difference = difference
  return greatest_difference
