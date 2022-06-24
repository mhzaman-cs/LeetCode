#<--------------------------- Maximum Sum Subarray of Size K (easy) --------------------------->#

# Grokking Passed
def max_sub_array_of_size_k(k, arr):
  startIndex, curSum, curMax = 0, 0, float('-inf')

  for endIndex in range(len(arr)):
    curSum += arr[endIndex]

    if endIndex >= k-1:
      curMax = max(curMax, curSum)
      curSum -= arr[startIndex]
      startIndex += 1
  return curMax


#<--------------------------- Smallest Subarray With a Greater Sum (easy) --------------------------->#

# Grokking Passed
def smallest_subarray_sum(s, arr):
  if s == 0:
    return 0
  startIndex, curSum, minLen, curLen = 0, 0, float('inf'), 0

  for endIndex in range(len(arr)):
    curSum += arr[endIndex]
    curLen += 1

    if curSum >= s:
      for i in range(endIndex - startIndex +1):
        if curSum >= s:
          minLen = min(curLen, minLen)
          curSum -= arr[startIndex]
          startIndex += 1
          curLen -= 1
  return minLen

# Leetcode Question 209: https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if (target == 0) or (sum(nums) < target):
            return 0

        startIndex, curSum, minLen, curLen = 0, 0, float('inf'), 0

        for endIndex in range(len(nums)):
            curSum += nums[endIndex]
            curLen += 1

            if curSum >= target:
                for i in range(endIndex - startIndex +1):
                    if curSum >= target:
                        minLen = min(curLen, minLen)
                        curSum -= nums[startIndex]
                        startIndex += 1
                        curLen -= 1
                    else:
                        break
        return minLen
