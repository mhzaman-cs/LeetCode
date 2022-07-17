#<--------------------------- Pair with Target Sum (easy) --------------------------->#

# Grokking Passed
def pair_with_targetsum(arr, target_sum):
  startIndex = 0
  endIndex = len(arr) - 1

  while endIndex > startIndex:
    curSum = arr[startIndex] + arr[endIndex]

    if curSum > target_sum:
      endIndex -= 1

    elif curSum == target_sum:
      return [startIndex, endIndex]
    else:
      startIndex += 1

  return [-1, -1]
