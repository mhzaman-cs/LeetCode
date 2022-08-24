#<--------------------------- Single Number (easy) --------------------------->#

# Grokking Passed
def find_single_number(arr):
  num = arr[0]
  n = len(arr)

  for i in range(1, n):
    num ^= arr[i]
  return num

def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))

main()


# Leetcode Question 136: https://leetcode.com/problems/single-number/
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    num = nums[0]
    n = len(nums)

    for i in range(1, n):
      num ^= nums[i]

    return num


#<--------------------------- Two Single Numbers (medium) --------------------------->#

# Grokking Passed
def find_single_numbers(nums):
  num1, num2 = 0, 0
  allNumsXOR = 0
  withBit, withoutBit = [], []

  for num in nums:
    allNumsXOR ^= num

  rightmostSetBit = allNumsXOR & -allNumsXOR

  for num in nums:
    if (num & rightmostSetBit):
      num1 ^= num
    else:
      num2 ^= num

  return [num1, num2]


def main():
  print('Single numbers are:' +
        str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
  print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))

main()


# Leetcode Question 260: https://leetcode.com/problems/single-number-iii/
class Solution:
  def singleNumber(self, nums: List[int]) -> List[int]:
    num1, num2 = 0, 0
    allNumsXOR = 0
    withBit, withoutBit = [], []

    for num in nums:
      allNumsXOR ^= num

    rightmostSetBit = allNumsXOR & -allNumsXOR

    for num in nums:
      if (num & rightmostSetBit):
        num1 ^= num
      else:
        num2 ^= num

    return [num1, num2]


#<--------------------------- Complement of Base 10 Number (medium) --------------------------->#

# Grokking Passed
def calculate_bitwise_complement(n):
  bitCount, num = 0, n

  while num > 0:
    bitCount += 1
    num = num >> 1

  fullBit = pow(2, bitCount) - 1
  return n ^ fullBit

def main():
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))

main()


# Leetcode Question 1009: https://leetcode.com/problems/complement-of-base-10-integer/
class Solution:
  def bitwiseComplement(self, n: int) -> int:
    if n == 0:
      return 1
    bitCount, num = 0, n

    while num > 0:
      bitCount += 1
      num = num >> 1

    fullBit = pow(2, bitCount) - 1
    return n ^ fullBit
