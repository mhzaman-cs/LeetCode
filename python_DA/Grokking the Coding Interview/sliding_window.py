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

#<--------------------------- Longest Substring with maximum K Distinct Characters (medium) --------------------------->#

# Grokking Passed
def longest_substring_with_k_distinct(str1, k):
  startIndex = strLen = maxLen = 0
  visitedChars = {} # Hashmap for the number of chars present

  if k == 0:
    return 0

  for endIndex in range(len(str1)):
    curChar = str1[endIndex]

    if curChar in visitedChars:
      visitedChars[curChar] += 1
      strLen += 1
      maxLen = max(maxLen, strLen)

    elif (k == 0):
      startChar = str1[startIndex]
      startCharsLeft = visitedChars.pop(startChar, 0)
      print([startIndex, endIndex, str1, startChar, startCharsLeft])
      maxLen = max(maxLen, strLen)

      while(startCharsLeft != 0):
        curStartChar = str1[startIndex]
        if curStartChar == startChar:
          startCharsLeft -= 1
        else:
          visitedChars[curStartChar] -= 1
        startIndex += 1
        strLen -= 1

      visitedChars[curChar] = 1
      strLen += 1
      maxLen = max(maxLen, strLen)

    else:
      visitedChars[curChar] = 1
      k -= 1
      strLen += 1
      maxLen = max(maxLen, strLen)


  return maxLen


#<--------------------------- Fruits into Baskets (medium) --------------------------->#

# Grokking Passed
def fruits_into_baskets(fruits):
  startIndex = maxLen = 0
  fruitsPicked = {}

  if len(fruits) == 0:
    return 0

  for endIndex in range(len(fruits)):
    curFruit = fruits[endIndex]

    if curFruit not in fruitsPicked:
      fruitsPicked[curFruit] = 0

    fruitsPicked[curFruit] += 1

    while(len(fruitsPicked) > 2):
      curStartFruit = fruits[startIndex]

      fruitsPicked[curStartFruit] -= 1

      if fruitsPicked[curStartFruit] == 0:
        del fruitsPicked[curStartFruit]

      startIndex += 1

    maxLen = max(maxLen, (endIndex - startIndex + 1))

  return maxLen


# Leetcode Question 904: https://leetcode.com/problems/fruit-into-baskets/
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        startIndex = maxLen = 0
        fruitsPicked = {}

        if len(fruits) == 0:
            return 0

        for endIndex in range(len(fruits)):
            curFruit = fruits[endIndex]

            if curFruit not in fruitsPicked:
                fruitsPicked[curFruit] = 0

            fruitsPicked[curFruit] += 1


            while(len(fruitsPicked) > 2):
                curStartFruit = fruits[startIndex]

                fruitsPicked[curStartFruit] -= 1

                if fruitsPicked[curStartFruit] == 0:
                    del fruitsPicked[curStartFruit]

                startIndex += 1


            maxLen = max(maxLen, (endIndex - startIndex + 1))

        return maxLen
