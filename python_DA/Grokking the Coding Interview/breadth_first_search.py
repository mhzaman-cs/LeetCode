#<--------------------------- Binary Tree Level Order Traversal (easy)  --------------------------->#

# Grokking Passed
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  result = []
  if root is None:
    return result

  Deque = deque()
  Deque.append(root)

  while Deque:
    lenDuq = len(Deque)
    curRow = []

    for _ in range(lenDuq):
      curNode = Deque.popleft()
      if curNode.left:
        Deque.append(curNode.left)
      if curNode.right:
        Deque.append(curNode.right)
      curRow.append(curNode.val)

    result.append(curRow)

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))

main()


# Leetcode Question 102: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      result = []
      if root is None:
        return result

      Deque = deque()
      Deque.append(root)

      while Deque:
        lenDuq = len(Deque)
        curRow = []

        for _ in range(lenDuq):
          curNode = Deque.popleft()
          if curNode.left:
            Deque.append(curNode.left)
          if curNode.right:
            Deque.append(curNode.right)
          curRow.append(curNode.val)

        result.append(curRow)

      return result


#<--------------------------- Reverse Level Order Traversal (easy) --------------------------->#

# Grokking Passed
from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = deque()

  Deque = deque()
  Deque.append(root)

  while Deque:
    lenDeq = len(Deque)
    curRow = []

    for _ in range(lenDeq):
      curNode = Deque.popleft()

      if curNode.left:
        Deque.append(curNode.left)
      if curNode.right:
        Deque.append(curNode.right)

      curRow.append(curNode.val)

    result.appendleft(curRow)

  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(traverse(root)))

main()


# Leetcode Question 107: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
      result = deque()

      if not root:
        return result

      Deque = deque()
      Deque.append(root)

      while Deque:
        lenDeq = len(Deque)
        curRow = []

        for _ in range(lenDeq):
          curNode = Deque.popleft()

          if curNode.left:
            Deque.append(curNode.left)
          if curNode.right:
            Deque.append(curNode.right)

          curRow.append(curNode.val)

        result.appendleft(curRow)

      return result


#<--------------------------- Zigzag Traversal (medium) --------------------------->#

# Grokking Passed
from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = []
  rowNum = 0
  Deque = deque()
  Deque.append(root)

  while Deque:
    lenDeq = len(Deque)
    curRow = deque()

    for _ in range(lenDeq):
      curNode = Deque.popleft()

      if curNode.left:
        Deque.append(curNode.left)
      if curNode.right:
        Deque.append(curNode.right)

      if rowNum%2 == 0:
        curRow.append(curNode.val)
      else:
        curRow.appendleft(curNode.val)

    result.append(list(curRow))
    rowNum += 1
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()


# Leetcode Question 103: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      result = []
      rowNum = 0

      if not root:
        return result
      Deque = deque()
      Deque.append(root)

      while Deque:
        lenDeq = len(Deque)
        curRow = deque()

        for _ in range(lenDeq):
          curNode = Deque.popleft()

          if curNode.left:
            Deque.append(curNode.left)
          if curNode.right:
            Deque.append(curNode.right)

          if rowNum%2 == 0:
            curRow.append(curNode.val)
          else:
            curRow.appendleft(curNode.val)

        result.append(list(curRow))
        rowNum += 1
      return result


#<--------------------------- Level Averages in a Binary Tree (easy) --------------------------->#

# Grokking Passed
from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
  result = []

  if not root:
    return result

  Deque = deque()
  Deque.append(root)

  while Deque:
    lenDeq = len(Deque)
    curSum = 0

    for _ in range(lenDeq):
      curNode = Deque.popleft()

      if curNode.left:
        Deque.append(curNode.left)
      if curNode.right:
        Deque.append(curNode.right)
      curSum += curNode.val

    result.append(curSum/lenDeq)
    curSum = 0
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))


main()


# Leetcode Question 637: https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
      result = []

      if not root:
        return result

      Deque = deque()
      Deque.append(root)

      while Deque:
        lenDeq = len(Deque)
        curSum = 0

        for _ in range(lenDeq):
          curNode = Deque.popleft()

          if curNode.left:
            Deque.append(curNode.left)
          if curNode.right:
            Deque.append(curNode.right)
          curSum += curNode.val

        result.append(curSum/lenDeq)
        curSum = 0
      return result


#<--------------------------- Minimum Depth of a Binary Tree (easy) --------------------------->#

# Grokking Passed
from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
  Deque = deque()
  minDepth = float('inf')
  curDepth = 0
  Deque.append(root)

  while Deque:
    lenDeq = len(Deque)
    curDepth += 1
    for _ in range(lenDeq):
      curNode = Deque.popleft()

      if curNode.left:
        Deque.append(curNode.left)
      if curNode.right:
        Deque.append(curNode.right)

      if not curNode.right and not curNode.left:
        minDepth = min(minDepth, curDepth)

  return minDepth


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()


# Leetcode Question 111: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
      if not root:
        return 0
      Deque = deque()
      minDepth = float('inf')
      curDepth = 0
      Deque.append(root)

      while Deque:
        lenDeq = len(Deque)
        curDepth += 1
        for _ in range(lenDeq):
          curNode = Deque.popleft()

          if curNode.left:
            Deque.append(curNode.left)
          if curNode.right:
            Deque.append(curNode.right)

          if not curNode.right and not curNode.left:
            minDepth = min(minDepth, curDepth)

      return minDepth


#<---------------------------Level Order Successor (easy) --------------------------->#

# Grokking Passed
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  if not root:
    return None

  Deque = deque()
  Deque.append(root)

  while Deque:
    lenDeq = len(Deque)

    for _ in range(lenDeq):
      curNode = Deque.popleft()

      if curNode == key:
        return Deque.popleft()

      if curNode.left:
        Deque.append(curNode.left)
      if curNode.right:
        Deque.append(curNode.right)

def main():
  root = TreeNode(1);
  root.left = TreeNode(2);
  root.right = TreeNode(3);
  root.left.left = TreeNode(4);
  root.left.right = TreeNode(5);

  result = find_successor(root, 3)
  if result:
    print(result.val)

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)

  result = find_successor(root, 9)
  if result:
    print(result.val)

  result = find_successor(root, 12)
  if result:
    print(result.val)


main()


#<--------------------------- Connect Level Order Siblings (medium) --------------------------->#

# Grokking Passed
from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # level order traversal using 'next' pointer
  def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
      current = nextLevelRoot
      nextLevelRoot = None
      while current:
        print(str(current.val) + " ", end='')
        if not nextLevelRoot:
          if current.left:
            nextLevelRoot = current.left
          elif current.right:
            nextLevelRoot = current.right
        current = current.next
      print()


def connect_level_order_siblings(root):
  if not root:
    return None

  Deque = deque()
  Deque.append(root)

  while Deque:
    lenDeq = len(Deque)

    for i in range(lenDeq):
      curNode = Deque.popleft()

      if curNode.left:
        Deque.append(curNode.left)
      if curNode.right:
        Deque.append(curNode.right)
      if lenDeq-i == 1:
        curNode.next = None
      else:
        curNode.next = Deque[0]


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_level_order_siblings(root)

  print("Level order traversal using 'next' pointer: ")
  root.print_level_order()


main()


# Leetcode Question 116: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
      if not root:
        return None

      Deque = deque()
      Deque.append(root)

      while Deque:
        lenDeq = len(Deque)

        for i in range(lenDeq):
          curNode = Deque.popleft()

          if curNode.left:
            Deque.append(curNode.left)
          if curNode.right:
            Deque.append(curNode.right)
          if lenDeq-i == 1:
            curNode.next = None
          else:
            curNode.next = Deque[0]

      return root
