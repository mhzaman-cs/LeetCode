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


#<--------------------------- Remove Duplicates (easy) --------------------------->#

# Grokking Passed
def remove_duplicates(arr):
  p1 = p2 = 0
  lenArr = len(arr)
  uniqueChar = arr[p1]
  uniqueCharCount = 1

  # p1 is for the next position where the last unique element was added
  # p2 is for traversing the list

  while (p2 < lenArr - 1):
    p2 += 1
    curChar = arr[p2]

    if curChar != uniqueChar:
      uniqueCharCount += 1
      p1 += 1
      arr[p1] = uniqueChar = curChar

  return uniqueCharCount


# Leetcode Question 26: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = p2 = 0
        lenArr = len(nums)
        uniqueChar = nums[p1]
        uniqueCharCount = 1

        # p1 is for the next position where the last unique element was added
        # p2 is for traversing the list

        while (p2 < lenArr - 1):
          p2 += 1
          curChar = nums[p2]

          if curChar != uniqueChar:
            uniqueCharCount += 1
            p1 += 1
            nums[p1] = uniqueChar = curChar

        return uniqueCharCount


#<--------------------------- Squaring a Sorted Array (easy) --------------------------->#

# Grokking Passed
def make_squares(arr):
  lenArr = len(arr)
  squares = [0] * lenArr
  leftP = 0
  largestSquareIndex = rightP = lenArr - 1

  while(leftP <= rightP):
    leftSquare = arr[leftP] ** 2
    rightSquare = arr[rightP] ** 2

    if leftSquare < rightSquare:
      squares[largestSquareIndex] = rightSquare
      largestSquareIndex -= 1
      rightP -= 1
    else:
      squares[largestSquareIndex] = leftSquare
      largestSquareIndex -= 1
      leftP += 1

  return squares


# Leetcode Question 977: https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lenArr = len(nums)
        squares = [0] * lenArr
        leftP = 0
        largestSquareIndex = rightP = lenArr - 1

        while(leftP <= rightP):
          leftSquare = nums[leftP] ** 2
          rightSquare = nums[rightP] ** 2

          if leftSquare < rightSquare:
            squares[largestSquareIndex] = rightSquare
            largestSquareIndex -= 1
            rightP -= 1
          else:
            squares[largestSquareIndex] = leftSquare
            largestSquareIndex -= 1
            leftP += 1

        return squares


#<--------------------------- Triplet Sum to Zero (medium) --------------------------->#

# Grokking Passed
def findTriplets(leftIndex, sortedArr, targetNum, lenArray, triplets):
  rightIndex = lenArray - 1

  while(leftIndex < rightIndex):
    curSum = sortedArr[leftIndex] + sortedArr[rightIndex]

    if curSum == targetNum:
      newTriplets = [-targetNum, sortedArr[leftIndex], sortedArr[rightIndex]]
      if newTriplets not in triplets:
        triplets.append([-targetNum, sortedArr[leftIndex], sortedArr[rightIndex]])
      leftIndex += 1
      rightIndex -= 1

    elif curSum < targetNum:
      leftIndex += 1

    else:
      rightIndex -= 1

def search_triplets(arr):
  sortedArr = sorted(arr)
  lenArray = len(sortedArr)
  triplets = []

  for startIndex in range(lenArray):
    findTriplets(startIndex+1, sortedArr, -sortedArr[startIndex], lenArray, triplets)

  return triplets


# Leetcode Question 15: https://leetcode.com/problems/3sum/
def findTriplets(leftIndex, sortedArr, targetNum, lenArray, triplets):
  rightIndex = lenArray - 1

  while(leftIndex < rightIndex):
    curSum = sortedArr[leftIndex] + sortedArr[rightIndex]

    if curSum == targetNum:
      newTriplets = [-targetNum, sortedArr[leftIndex], sortedArr[rightIndex]]
      if newTriplets not in triplets:
        triplets.append(newTriplets)
      leftIndex += 1
      rightIndex -= 1

    elif curSum < targetNum:
      leftIndex += 1

    else:
      rightIndex -= 1


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      sortedArr = sorted(nums)
      lenArray = len(sortedArr)
      triplets = []

      for startIndex in range(lenArray):
        findTriplets(startIndex+1, sortedArr, -sortedArr[startIndex], lenArray, triplets)

      return triplets


#<--------------------------- Triplet Sum Close to Target (medium) --------------------------->#

# Grokking Passed
def triplet_sum_close_to_target(arr, target_sum):
  sortedArr, minDiff, lenArr = sorted(arr), float('inf'), len(arr)

  for i in range(len(sortedArr)-2):
    leftp = i + 1
    rightp = lenArr - 1

    while(leftp < rightp):
      curSum = sortedArr[i] + sortedArr[leftp] + sortedArr[rightp]
      curDiff = target_sum - curSum

      if curDiff == 0:
        return target_sum

      if abs(minDiff) > abs(curDiff) or ((abs(minDiff) == abs(curDiff)) and target_sum - minDiff > curSum):
        minDiff = curDiff

      if curSum < target_sum:
        leftp += 1

      if curSum > target_sum:
        rightp -= 1

  return target_sum - minDiff


# Leetcode Question 16: https://leetcode.com/problems/3sum-closest/
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
      sortedArr, minDiff, lenArr = sorted(nums), float('inf'), len(nums)

      for i in range(len(sortedArr)-2):
        leftp = i + 1
        rightp = lenArr - 1

        while(leftp < rightp):
          curSum = sortedArr[i] + sortedArr[leftp] + sortedArr[rightp]
          curDiff = target - curSum

          if curDiff == 0:
            return target

          if abs(minDiff) > abs(curDiff) or ((abs(minDiff) == abs(curDiff)) and target - minDiff > curSum):
            minDiff = curDiff

          if curSum < target:
            leftp += 1

          if curSum > target:
            rightp -= 1

      return target - minDiff
