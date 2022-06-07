# Question 100 Link: https://leetcode.com/problems/same-tree/

# Recursive Solution:
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
        if ((q != None) and (p != None)):
            return (q.val == p.val) and self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        elif (q == None) and (p == None):
            return True
        else:
            return False

# Iterative Solution Depth First Search:
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

# Question 1 Link: https://leetcode.com/problems/two-sum/

# Original Solution
class Solution(object):
    def twoSum(self, nums, target):

        diff_hash = {} # Difference of the numbers to the target
        len_list = len(nums)

        for i in range(len_list):
            diff_target = target - nums[i]
            if (diff_target in diff_hash) and (diff_target == nums[i]) :
                return [diff_hash[diff_target], i] # If 2 things need the same number to reach the target and they are equal to the, they can use eachother
            else:
                diff_hash[diff_target] = i

        # Now we have an insurance of uniqueness as the previous case would have returned any non unique value

        print(diff_hash)
        for num_needed in diff_hash:
            if (num_needed in nums) and (diff_hash[num_needed] != nums.index(num_needed)):
                return [diff_hash[num_needed], nums.index(num_needed)]


# Easy Question 643 https://leetcode.com/problems/maximum-average-subarray-i/

# Better Memory allocation
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum, start_index = 0.0, 0
        curr_max = float('-inf')
        list_len = len(nums)

        for index in range(list_len):
            curr_sum += nums[index]

            if ((index - start_index + 1) == k):
                curr_max = max((curr_sum/k), curr_max)
                curr_sum -= nums[start_index]
                start_index += 1

        return curr_max

# Better Time allocation
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum, start_index = 0.0, 0
        average_list = []
        list_len = len(nums)

        for index in range(list_len):
            curr_sum += nums[index]

            if ((index - start_index + 1) == k):
                average_list.append(curr_sum/k)
                curr_sum -= nums[start_index]
                start_index += 1

        return max(average_list)
