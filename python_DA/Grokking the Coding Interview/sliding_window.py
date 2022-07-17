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


#<--------------------------- Longest Substring with Distinct Characters (hard) --------------------------->#

# Grokking Passed
def non_repeat_substring(str):
  visitedChars = {} # Key value of char and pos
  startIndex = maxLen = 0

  for endIndex in range(len(str)):
    curChar = str[endIndex]

    if curChar in visitedChars:
      removePos = visitedChars[curChar]

      while(removePos >= startIndex):
        del visitedChars[str[startIndex]]
        startIndex += 1

    visitedChars[curChar] = endIndex
    maxLen = max(maxLen, endIndex - startIndex + 1)

  return maxLen


# Leetcode Question 3: https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visitedChars = {} # Key value of char and pos
        startIndex = maxLen = 0

        for endIndex in range(len(s)):
            curChar = s[endIndex]

            if curChar in visitedChars:
                removePos = visitedChars[curChar]


                while(removePos >= startIndex):
                    del visitedChars[s[startIndex]]
                    startIndex += 1


            visitedChars[curChar] = endIndex
            maxLen = max(maxLen, endIndex - startIndex + 1)

        return maxLen


#<--------------------------- Longest Substring with Same Letters after Replacement (hard) --------------------------->#

# Grokking Passed
def length_of_longest_substring(str1, k):
  startIndex = maxLen = maxFreqCurChar = 0
  vistiedChars = {} # Notes the frequency of the chars

  for endIndex, curChar in enumerate(str1):
    if curChar not in vistiedChars:
      vistiedChars[curChar] = 0

    vistiedChars[curChar] += 1

    maxFreqCurChar = max(maxFreqCurChar, vistiedChars[curChar])

    if (endIndex - startIndex + 1 - maxFreqCurChar > k):
      vistiedChars[str1[startIndex]] -= 1
      startIndex += 1

    maxLen = max(maxLen, endIndex - startIndex + 1)

  return maxLen


# Leetcode Question 424: https://leetcode.com/problems/longest-repeating-character-replacement/
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        startIndex = maxLen = maxFreqCurChar = 0
        vistiedChars = {} # Notes the frequency of the chars

        for endIndex, curChar in enumerate(s):
            if curChar not in vistiedChars:
                vistiedChars[curChar] = 0

            vistiedChars[curChar] += 1

            maxFreqCurChar = max(maxFreqCurChar, vistiedChars[curChar])

            if (endIndex - startIndex + 1 - maxFreqCurChar > k):
                vistiedChars[s[startIndex]] -= 1
                startIndex += 1

            maxLen = max(maxLen, endIndex - startIndex + 1)


        return maxLen


#<--------------------------- Longest Subarray with Ones after Replacement (hard) --------------------------->#

# Grokking Passed
def length_of_longest_substring(arr, k):
  startIndex = maxLen = curNumOnes = 0

  for endIndex, curNum in enumerate(arr):
    if curNum == 1:
      curNumOnes += 1

    if (endIndex - startIndex + 1 - curNumOnes) > k:
      if arr[startIndex] == 1: curNumOnes -= 1
      startIndex += 1

    maxLen = max(maxLen, endIndex - startIndex + 1)
  return maxLen


# Leetcode Question 1004: https://leetcode.com/problems/max-consecutive-ones-iii/
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        startIndex = maxLen = curNumOnes = 0

        for endIndex, curNum in enumerate(nums):
            if curNum == 1: curNumOnes += 1

            if (endIndex - startIndex + 1 - curNumOnes) > k:
                if nums[startIndex] == 1: curNumOnes -= 1
                startIndex += 1

            maxLen = max(maxLen, endIndex - startIndex + 1)

        return maxLen


#<--------------------------- Permutation in a String (hard) --------------------------->#

# Grokking Passed
def find_permutation(str1, pattern):
  sortedPattern = "".join(sorted(pattern))
  patternLen = len(pattern)
  startIndex = 0
  auxArray = ""

  for endIndex, curChar in enumerate(str1):
    auxArray += curChar

    if (endIndex - startIndex + 1) == patternLen:
      if "".join(sorted(auxArray)) == sortedPattern:
        return True

      startIndex += 1
      auxArray = auxArray[1:]

  return False


# Leetcode Question 567: https://leetcode.com/problems/permutation-in-string/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sortedPattern = "".join(sorted(s1))
        patternLen = len(s1)
        startIndex = 0
        auxArray = ""

        for endIndex, curChar in enumerate(s2):
            auxArray += curChar

            if (endIndex - startIndex + 1) == patternLen:
                if "".join(sorted(auxArray)) == sortedPattern:
                    return True

                startIndex += 1
                auxArray = auxArray[1:]

        return False
