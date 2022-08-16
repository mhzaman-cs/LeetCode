#<--------------------------- Subsets (easy) --------------------------->#

# Grokking Passed
def find_subsets(nums):
  subsets = []
  subsets.append([])

  for i in nums:
    n = len(subsets)
    for j in range(n):
      subsets.append(subsets[j]+[i])
  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()


# Leetcode Question 78: https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      subsets = []
      subsets.append([])

      for i in nums:
        n = len(subsets)
        for j in range(n):
          subsets.append(subsets[j]+[i])
      return subsets


#<--------------------------- Subsets With Duplicates (easy) --------------------------->#

# Grokking Passed
def find_subsets(nums):
  subsets = []
  lenPrevSub = 1
  prev = None
  subsets.append([])
  nums.sort()

  for i in nums:
    n = len(subsets)
    curSub = 0
    startDupIndex = 0
    if i == prev:
      startDupIndex = n-lenPrevSub

    for j in range(startDupIndex, n):
      subsets.append(subsets[j] + [i])
      curSub += 1
    lenPrevSub = curSub
    prev = i
  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()


# Leetcode Question 90: https://leetcode.com/problems/subsets-ii/
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
      subsets = []
      lenPrevSub = 1
      prev = None
      subsets.append([])
      nums.sort()

      for i in nums:
        n = len(subsets)
        curSub = 0
        startDupIndex = 0
        if i == prev:
          startDupIndex = n-lenPrevSub

        for j in range(startDupIndex, n):
          subsets.append(subsets[j] + [i])
          curSub += 1
        lenPrevSub = curSub
        prev = i
      return subsets


#<--------------------------- Permutations (medium) --------------------------->#

# Grokking Passed
from collections import deque

def find_permutations(nums):
  if not nums:
    return []

  curPermutations = deque()
  curPermutations.append([])
  lenNums = len(nums)

  result = []

  for curNum in nums:
    lenCurPerm  = len(curPermutations)

    for _ in range(lenCurPerm):
      curPerm = curPermutations.popleft()
      curPermLen = len(curPerm)+1

      for j in range(curPermLen):
        curPermList = list(curPerm)
        curPermList.insert(j, curNum)
        if len(curPermList) == lenNums:
          result.append(curPermList)
        else:
          curPermutations.append(curPermList)

  return result


def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))

main()


# Leetcode Question 46: https://leetcode.com/problems/permutations/
class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    if not nums:
      return []

    curPermutations = deque()
    curPermutations.append([])
    lenNums = len(nums)

    result = []

    for curNum in nums:
      lenCurPerm  = len(curPermutations)

      for _ in range(lenCurPerm):
        curPerm = curPermutations.popleft()
        curPermLen = len(curPerm)+1

        for j in range(curPermLen):
          curPermList = list(curPerm)
          curPermList.insert(j, curNum)
          if len(curPermList) == lenNums:
            result.append(curPermList)
          else:
            curPermutations.append(curPermList)

    return result


#<--------------------------- Permutations (medium) --------------------------->#

# Grokking Passed
def find_letter_case_string_permutations(curStr):
  permutations = []
  lenStr = len(curStr)
  permutations.append(curStr)

  for i in range(lenStr):

    curChar = curStr[i]
    if curChar.isalpha():

      lenPerm = len(permutations)

      for j in range(lenPerm):
        lstPerm = list(permutations[j])
        lstPerm[i] = lstPerm[i].swapcase()
        permutations.append(''.join(lstPerm))

  return permutations


def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()


# Leetcode Question 46: https://leetcode.com/problems/permutations/
class Solution:
  def letterCasePermutation(self, s: str) -> List[str]:
    permutations = []
    lenStr = len(s)
    permutations.append(s)

    for i in range(lenStr):

      curChar = s[i]
      if curChar.isalpha():

        lenPerm = len(permutations)

        for j in range(lenPerm):
          lstPerm = list(permutations[j])
          lstPerm[i] = lstPerm[i].swapcase()
          permutations.append(''.join(lstPerm))

    return permutations


#<--------------------------- Balanced Parentheses (hard) --------------------------->#

# Grokking Passed
def generate_valid_parentheses_rec(num, openCount, closeCount, parenthesesString, result):
  if openCount == num and closeCount == num:
    result.append(parenthesesString)

  else:
    if openCount < num:
      generate_valid_parentheses_rec(num, openCount+1, closeCount, parenthesesString+'(', result)

    if openCount > closeCount:
      generate_valid_parentheses_rec(num, openCount, closeCount+1, parenthesesString+')', result)

def generate_valid_parentheses(num):
  result = []
  lstParentheses = []
  generate_valid_parentheses_rec(num, 0, 0, '', result)
  return result

def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))


main()


# Leetcode Question 22: https://leetcode.com/problems/generate-parentheses/
def generate_valid_parentheses_rec(num, openCount, closeCount, parenthesesString, result):
  if openCount == num and closeCount == num:
    result.append(parenthesesString)

  else:
    if openCount < num:
      generate_valid_parentheses_rec(num, openCount+1, closeCount, parenthesesString+'(', result)

    if openCount > closeCount:
      generate_valid_parentheses_rec(num, openCount, closeCount+1, parenthesesString+')', result)


class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    result = []
    lstParentheses = []
    generate_valid_parentheses_rec(n, 0, 0, '', result)
    return result


#<--------------------------- Unique Generalized Abbreviations (hard) --------------------------->#

# Grokking Passed
def generate_generalized_abbreviation(word):
  result = []
  generate_abbreviation_recursive(word, list(), 0, 0, result)
  return result

def generate_abbreviation_recursive(word, abWord, start, count, result):

  if start == len(word):
    if count != 0:
      abWord.append(str(count))
    result.append(''.join(abWord))

  else:
    generate_abbreviation_recursive(word, list(abWord), start+1, count+1, result)

    if count != 0:
      abWord.append(str(count))
    newWord = list(abWord)
    newWord.append(word[start])
    generate_abbreviation_recursive(word, newWord, start+1, 0, result)


def main():
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("BAT")))
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("code")))


main()
