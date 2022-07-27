#<--------------------------- Cyclic Sort (easy)  --------------------------->#

# Grokking Passed
def cyclic_sort(nums):
  i = 0
  lenNums = len(nums)
  while (i < lenNums):
    if nums[i] == i+1:
      i+=1
    else:
      nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

  return nums


#<--------------------------- Find the Missing Number (easy)  --------------------------->#

# Grokking Passed
def find_missing_number(nums):
  nums.sort()
  lenNums = len(nums)
  i = 0

  while(i<lenNums):
    if i != nums[i]:
      return i
    i+=1
  return lenNums


# Leetcode Question 268: https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      nums.sort()
      lenNums = len(nums)
      i = 0

      while(i<lenNums):
        if i != nums[i]:
          return i
        i+=1

      return lenNums


#<--------------------------- Find all Missing Numbers (easy)  --------------------------->#

# Grokking Passed
def find_missing_numbers(nums):
  missingNumbers = []
  i, lenNums = 0, len(nums)

  while(i < lenNums):
    j = nums[i] - 1
    if nums[j] != nums[i]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1

  for i in range(lenNums):
    if nums[i] != i +1:
       missingNumbers.append(i+1)

  return missingNumbers


# Leetcode Question 448: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
      missingNumbers = []
      i, lenNums = 0, len(nums)

      while(i < lenNums):
        j = nums[i] - 1
        if nums[j] != nums[i]:
          nums[i], nums[j] = nums[j], nums[i]
        else:
          i += 1

      for i in range(lenNums):
        if nums[i] != i +1:
           missingNumbers.append(i+1)

      return missingNumbers


#<--------------------------- Find the Duplicate Number (easy)  --------------------------->#

# Grokking Passed
def find_duplicate(nums):
  i, lenNums = 0, len(nums)

  while(i < lenNums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1

  return nums[-1]


# Leetcode Question 287: https://leetcode.com/problems/find-the-duplicate-number/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
      i, lenNums = 0, len(nums)

      while(i < lenNums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
          nums[i], nums[j] = nums[j], nums[i]
        else:
          i += 1
      return nums[-1]


#<--------------------------- Find all Duplicate Numbers (easy)  --------------------------->#

# Grokking Passed
def find_all_duplicates(nums):
  duplicateNumbers = []
  i, lenNums = 0, len(nums)

  while(i < lenNums):
    j = nums[i] - 1

    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1

  for i in range(lenNums):
    if nums[i] != i+1:
      duplicateNumbers.append(nums[i])
  return duplicateNumbers


# Leetcode Question 442: https://leetcode.com/problems/find-all-duplicates-in-an-array/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
      duplicateNumbers = []
      i, lenNums = 0, len(nums)

      while(i < lenNums):
        j = nums[i] - 1

        if nums[i] != nums[j]:
          nums[i], nums[j] = nums[j], nums[i]
        else:
          i += 1

      for i in range(lenNums):
        if nums[i] != i+1:
          duplicateNumbers.append(nums[i])
      return duplicateNumbers
