#<--------------------------- Smallest Subarray With a Greater Sum (easy) --------------------------->#

# Grokking Passed
def binary_search(arr, key):
  start, end = 0, len(arr)-1
  isAssending = arr[start] < arr[end]

  while(end >= start):
    curCenter =  int((start + end)/2)
    curNum = arr[curCenter]

    if curNum == key:
      return curCenter

    if not isAssending:
      if curNum > key:
        start = curCenter + 1
      else:
        end = curCenter - 1

    else:
      if curNum < key:
        start = curCenter + 1
      else:
        end = curCenter - 1

  return -1

def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))


main()


# Leetcode Question 704: https://leetcode.com/problems/binary-search/
class Solution:
  def search(self, nums: List[int], target: int) -> int:
    start, end = 0, len(nums)-1
    isAssending = nums[start] < nums[end]

    while(end >= start):
      curCenter =  int((start + end)/2)
      curNum = nums[curCenter]

      if curNum == target:
        return curCenter

      if not isAssending:
        if curNum > target:
          start = curCenter + 1
        else:
          end = curCenter - 1

      else:
        if curNum < target:
          start = curCenter + 1
        else:
          end = curCenter - 1

    return -1


#<--------------------------- Ceiling of a Number (medium) --------------------------->#

# Grokking Passed
def search_ceiling_of_a_number(arr, key):
  start, end = 0, len(arr)-1

  while (end >= start):
    curMid = int((start+end)/2)
    curNum = arr[curMid]

    if curNum >= key and (curMid == 0 or curMid > 0 and key > arr[curMid-1]):
      return curMid

    if curNum > key:
      end = curMid - 1

    else:
      start = curMid + 1
  return -1


def main():
  print(search_ceiling_of_a_number([4, 6, 10], 6))
  print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
  print(search_ceiling_of_a_number([4, 6, 10], 17))
  print(search_ceiling_of_a_number([4, 6, 10], -1))


main()


# Leetcode Question 35: https://leetcode.com/problems/search-insert-position/
class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    start, end = 0, len(nums)-1

    while (end >= start):
      curMid = int((start+end)/2)
      curNum = nums[curMid]

      if curNum >= target and (curMid == 0 or curMid > 0 and target > nums[curMid-1]):
        return curMid

      if curNum > target:
        end = curMid - 1

      else:
        start = curMid + 1
    return len(nums)


#<--------------------------- Next Letter (medium) --------------------------->#

# Grokking Passed
def search_next_letter(letters, key):
  start, end = 0, len(letters)-1


  while(end>=start):
    mid = start + (end - start) // 2
    curLetter = letters[mid]

    if key >= curLetter:
      start = mid + 1
    else:
      end = mid - 1

  return letters[start%len(letters)]


def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()


# Leetcode Question 744: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
class Solution:
  def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    start, end = 0, len(letters)-1

    while(end>=start):
      mid = start + (end - start) // 2
      curLetter = letters[mid]

      if target >= curLetter:
        start = mid + 1
      else:
        end = mid - 1

    return letters[start%len(letters)]


#<--------------------------- Number Range (medium) --------------------------->#

# Grokking Passed
def find_range(arr, key):
  result = [- 1, -1]
  start, end = 0, len(arr)-1
  foundPos = -1
  n = end

  while(end>=start):
    mid = (start+end)//2
    curNum = arr[mid]

    if curNum == key:
      foundPos = mid
      break
    if curNum > key:
      end = mid - 1
    else:
      start = mid + 1

  if foundPos == -1:
    return result

  startRep = endRep = foundPos

  while(startRep >= 0):
    if key != arr[startRep]:
      break
    startRep -= 1

  while(endRep <= n):
    if key != arr[endRep]:
      break
    endRep += 1

  return [startRep+1, endRep-1]

def main():
  print(find_range([4, 6, 6, 6, 9], 6))
  print(find_range([1, 3, 8, 10, 15], 10))
  print(find_range([1, 3, 8, 10, 15], 12))


main()


# Leetcode Question 34: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    result = [- 1, -1]
    start, end = 0, len(nums)-1
    foundPos = -1
    n = end

    while(end>=start):
      mid = (start+end)//2
      curNum = nums[mid]

      if curNum == target:
        foundPos = mid
        break
      if curNum > target:
        end = mid - 1
      else:
        start = mid + 1

    if foundPos == -1:
      return result

    startRep = endRep = foundPos

    while(startRep >= 0):
      if target != nums[startRep]:
        break
      startRep -= 1

    while(endRep <= n):
      if target != nums[endRep]:
        break
      endRep += 1

    return [startRep+1, endRep-1]


#<--------------------------- Search in a Sorted Infinite Array (medium) --------------------------->#

# Grokking Passed
class ArrayReader:

  def __init__(self, arr):
    self.arr = arr

  def get(self, index):
    if index >= len(self.arr):
      return math.inf
    return self.arr[index]


def search_in_infinite_array(reader, key):
  start, end = 0, 1
  while reader.get(end) < key:
    newStart = end + 1
    end += (end - start + 1) * 2
    start = newStart

  while(end>=start):
    mid = start + (end - start) // 2
    curNum = reader.get(mid)

    if curNum == key:
      return mid
    if curNum > key:
      end = mid - 1
    else:
      start = mid + 1

  return -1

def main():
  reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
  print(search_in_infinite_array(reader, 16))
  print(search_in_infinite_array(reader, 11))
  reader = ArrayReader([1, 3, 8, 10, 15])
  print(search_in_infinite_array(reader, 15))
  print(search_in_infinite_array(reader, 200))


main()


#<--------------------------- Minimum Difference Element (medium) --------------------------->#

# Grokking Passed
def search_min_diff_element(arr, key):
  start, end = 0, len(arr)-1

  if key > arr[end]:
    return arr[end]

  if key < arr[start]:
    return arr[start]

  while(end>=start):
    mid = start + (end - start)//2
    curNum = arr[mid]

    if curNum == key:
      return curNum
    if curNum < key:
      start = mid + 1
    else:
      end = mid - 1

  startNum = arr[start]
  endNum = arr[end]
  
  if abs(key - startNum) < abs(key - endNum):
    return startNum
  else:
    return endNum

def main():
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))


main()


#<--------------------------- Bitonic Array Maximum (easy) --------------------------->#

# Grokking Passed
def find_max_in_bitonic_array(arr):
  start, end = 0, len(arr)-1

  if end == 1: 
    return arr[end]
  while(start < end):
    mid = start + (end - start)//2
    if arr[mid] > arr[mid + 1]:
      end = mid
    else:
      start = mid + 1
  return arr[end]


def main():
  print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
  print(find_max_in_bitonic_array([3, 8, 3, 1]))
  print(find_max_in_bitonic_array([1, 3, 8, 12]))
  print(find_max_in_bitonic_array([10, 9, 8]))


main()
