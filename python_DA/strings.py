class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s==s[::-1]

# Question 680 (Easy) Link: https://leetcode.com/problems/valid-palindrome-ii/
class Solution(object):
    def validPalindrome(self, s):
        p_start = 0
        p_end = len(s) - 1
        count = 0

        while (p_start < p_end):

            if s[p_start]!=s[p_end]:
                string1=s[:p_start]+s[p_start+1:]
                string2=s[:p_end]+s[p_end+1:]
                return string1==string1[::-1] or string2==string2[::-1]

            p_start += 1
            p_end -= 1


        return True



class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use 1D DP
        # dp[i] records the longestValidParenthese EXACTLY ENDING at s[i]
        dp = [0 for x in xrange(len(s))]
        max_to_now = 0
        for i in xrange(1,len(s)):
            if s[i] == ')':
                # case 1: ()()
                if s[i-1] == '(':
                    # add nearest parentheses pairs + 2
                    dp[i] = dp[i-2] + 2
                # case 2: (())
                # i-dp[i-1]-1 is the index of last "(" not paired until this ")"
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    if dp[i-1] > 0: # content within current matching pair is valid
                    # add nearest parentheses pairs + 2 + parentheses before last "("
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                    else:
                    # otherwise is 0
                        dp[i] = 0
                max_to_now = max(max_to_now, dp[i])
        return max_to_now



class Solution(object):
    def minMoves(self, nums, limit):
        n = len(nums)
        overlay_arr = [0] * (2*limit+2)
        for i in range(n//2):
            left_boundary = min(nums[i], nums[n-1-i]) + 1
            no_move_value = nums[i] + nums[n-1-i]
            right_boundary = max(nums[i], nums[n-1-i]) + limit
            overlay_arr[left_boundary] -= 1
            overlay_arr[no_move_value] -= 1
            overlay_arr[no_move_value+1] += 1
            overlay_arr[right_boundary+1] += 1
        curr_moves = n   #initial assumption of two moves for each pair
        res = float("inf")
		# start Sweeping
        for i in range(2, 2*limit+1):
            curr_moves += overlay_arr[i]
            res = min(res, curr_moves)
        return res

class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        return str(x) == str(x)[::-1]

class Solution(object):
    def firstUniqChar(self, s):
        visited = set()

        for i in range(len(s)):
            if not (s[i] in visited):
                visited.add(s[i])

                if (s.count(s[i])) == 1:
                    return i

        return -1

class Solution(object):
    def longestCommonPrefix(self, strs):
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i))==1:
                prefix += i[0]
            else:
                break
        return prefix

class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)

class Solution(object):
    def minMoves(self, nums, limit):
        n = len(nums)
        overlay_arr = [0] * (2*limit+2)
        for i in range(n//2):
            left_boundary = min(nums[i], nums[n-1-i]) + 1
            no_move_value = nums[i] + nums[n-1-i]
            right_boundary = max(nums[i], nums[n-1-i]) + limit
            overlay_arr[left_boundary] -= 1
            overlay_arr[no_move_value] -= 1
            overlay_arr[no_move_value+1] += 1
            overlay_arr[right_boundary+1] += 1
        curr_moves = n   #initial assumption of two moves for each pair
        res = float("inf")
		# start Sweeping
        for i in range(2, 2*limit+1):
            curr_moves += overlay_arr[i]
            res = min(res, curr_moves)
        return res

class Solution(object):
    def longestCommonPrefix(self, strs):
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i))==1:
                prefix += i[0]
            else:
                break
        return prefix

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use 1D DP
        # dp[i] records the longestValidParenthese EXACTLY ENDING at s[i]
        dp = [0 for x in xrange(len(s))]
        max_to_now = 0
        for i in xrange(1,len(s)):
            if s[i] == ')':
                # case 1: ()()
                if s[i-1] == '(':
                    # add nearest parentheses pairs + 2
                    dp[i] = dp[i-2] + 2
                # case 2: (())
                # i-dp[i-1]-1 is the index of last "(" not paired until this ")"
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    if dp[i-1] > 0: # content within current matching pair is valid
                    # add nearest parentheses pairs + 2 + parentheses before last "("
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                    else:
                    # otherwise is 0
                        dp[i] = 0
                max_to_now = max(max_to_now, dp[i])
        return max_to_now

class Solution(object):
    def longestCommonPrefix(self, strs):
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i))==1:
                prefix += i[0]
            else:
                break
        return prefix
