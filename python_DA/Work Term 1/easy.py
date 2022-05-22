# Question 100 Link: https://leetcode.com/problems/same-tree/
# Definition for a binary tree node.

# Recursive Solution:
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if ((q != None) and (p != None)):
            return (q.val == p.val) and self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        elif (q == None) and (p == None):
            return True
        else:
            return False

# Iterative Solution Depth First Search
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        stack = [(p, q)]

        while stack:
            p_tree, q_tree = stack.pop()
            if ((q_tree == None) and (p_tree == None)):
                continue
            elif ((q_tree == None) or (p_tree == None)):
                return False
            elif (q_tree.val != p_tree.val):
                return False
            else:
                stack.append((p_tree.right, q_tree.right))
                stack.append((p_tree.left, q_tree.left))

        return True


# Iterative Solution Breath First Search
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        Deque = deque([(p, q)])

        while Deque:
            p_tree, q_tree = Deque.popleft()
            if ((q_tree == None) and (p_tree == None)):
                continue
            elif ((q_tree == None) or (p_tree == None)):
                return False
            elif (q_tree.val != p_tree.val):
                return False
            else:
                Deque.append((p_tree.right, q_tree.right))
                Deque.append((p_tree.left, q_tree.left))

        return True
