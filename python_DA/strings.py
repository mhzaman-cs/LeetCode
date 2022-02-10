class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s==s[::-1]


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
        
