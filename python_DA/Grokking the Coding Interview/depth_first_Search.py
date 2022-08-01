#<--------------------------- Binary Tree Path Sum (easy) --------------------------->#

# Grokking Passed
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def has_path(root, sum):

  if not root:
    return False

  if not root.left and not root.right and root.val == sum: return True

  return has_path(root.right, sum - root.val) or has_path(root.left, sum - root.val)

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(has_path(root, 23)))
  print("Tree has path: " + str(has_path(root, 16)))


main()


# Leetcode Question 112: https://leetcode.com/problems/path-sum/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right and root.val == targetSum:
            return True

        targetSum -= root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


#<--------------------------- All Paths for a Sum (medium) --------------------------->#

# Grokking Passed
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_paths_lst(root, leftsum, allPaths, curPath):
  if root is None:
    return
  if leftsum == root.val and not root.right and not root.left:
      allPaths.append(curPath + [root.val])
  else:
    find_paths_lst(root.right, leftsum - root.val, allPaths, curPath + [root.val])
    find_paths_lst(root.left, leftsum - root.val, allPaths, curPath + [root.val])

def find_paths(root, sum):
  allPaths = []

  if not root:
    return allPaths
  find_paths_lst(root, sum, allPaths, [])
  return allPaths


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))


main()


# Leetcode Question 113: https://leetcode.com/problems/path-sum-ii/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths_lst(root, leftsum, allPaths, curPath):
  if root is None:
    return
  if leftsum == root.val and not root.right and not root.left:
      allPaths.append(curPath + [root.val])
  else:
    find_paths_lst(root.right, leftsum - root.val, allPaths, curPath + [root.val])
    find_paths_lst(root.left, leftsum - root.val, allPaths, curPath + [root.val])


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
      allPaths = []

      if not root:
        return allPaths
      find_paths_lst(root, targetSum, allPaths, [])
      return allPaths


#<--------------------------- Sum of Path Numbers (medium) --------------------------->#

# Grokking Passed
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_sum_of_curNode(curNode, curSum, overallSum):
  if not curNode:
    return 0

  if curNode.right is None and curNode.left is None:
    return ((curSum * 10) + curNode.val)

  else:
    return find_sum_of_curNode(curNode.left, ((curSum * 10) + curNode.val), overallSum) + find_sum_of_curNode(curNode.right, ((curSum * 10) + curNode.val), overallSum)

def find_sum_of_path_numbers(root):
  if not root:
    return 0

  return find_sum_of_curNode(root, 0, 0)



def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()


# Leetcode Question 129: https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_curNode(curNode, curSum, overallSum):
  if not curNode:
    return 0

  if curNode.right is None and curNode.left is None:
    return ((curSum * 10) + curNode.val)

  else:
    return find_sum_of_curNode(curNode.left, ((curSum * 10) + curNode.val), overallSum) + find_sum_of_curNode(curNode.right, ((curSum * 10) + curNode.val), overallSum)


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
      if not root:
        return 0

      return find_sum_of_curNode(root, 0, 0)


#<--------------------------- Path With Given Sequence (medium) --------------------------->#

# Grokking Passed
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def is_path(curNode, sequence, curIndex, lenSeq):
  if not curNode:
    return lenSeq == curIndex

  if sequence[curIndex] == curNode.val:
    return True and (is_path(curNode.left, sequence, curIndex + 1, lenSeq) or is_path(curNode.right, sequence, curIndex + 1, lenSeq))
  else:
    return False


def find_path(root, sequence):
  if not root:
    return len(sequence) == 0
  return is_path(root, sequence, 0, len(sequence))


def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()


#<--------------------------- Count Paths for a Sum (medium) --------------------------->#

# Grokking Passed
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def count_paths_recursive(curNode, S, curPath):
  if not curNode:
    return 0

  curPath.append(curNode.val)
  pathSum = pathCount = 0

  for i in range(len(curPath)-1, -1, -1):
    pathSum += curPath[i]

    if pathSum == S:
      pathCount += 1

  pathCount += count_paths_recursive(curNode.left, S, curPath)
  pathCount += count_paths_recursive(curNode.right, S, curPath)

  del curPath[-1]

  return pathCount

def count_paths(root, S):
  return count_paths_recursive(root, S, [])

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()


# Leetcode Question 437: https://leetcode.com/problems/path-sum-iii/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths_recursive(curNode, S, curPath):
  if not curNode:
    return 0

  curPath.append(curNode.val)
  pathSum = pathCount = 0

  for i in range(len(curPath)-1, -1, -1):
    pathSum += curPath[i]

    if pathSum == S:
      pathCount += 1

  pathCount += count_paths_recursive(curNode.left, S, curPath)
  pathCount += count_paths_recursive(curNode.right, S, curPath)

  del curPath[-1]

  return pathCount


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return count_paths_recursive(root, targetSum, [])
