# Question 10 (Hard) Link: https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(1, len(p)):
            dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == '*':
                    dp[i + 1][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1]
                    if p[i - 1] == s[j] or p[i - 1] == '.':
                        dp[i + 1][j + 1] |= dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')
        return dp[-1][-1]

# Question 70 (Easy) Link: https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def maxSubArray(self, nums):
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum

# Question 509 (Easy) Link: https://leetcode.com/problems/fibonacci-number/

class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        res = [0 for i in xrange(n)]
        res[0], res[1] = 1, 2
        for i in xrange(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]

# Question 53 (Easy) Link: https://leetcode.com/problems/maximum-subarray/
class Solution(object):
    def fib(self, n):
        if (n < 2):
            if (n == 0):
                return 0
            else:
                return 1
        else:
            first_num = 1
            second_num = 1
            for x in range(n - 2):
                sec_holder = first_num
                first_num = second_num
                second_num = sec_holder + second_num

            return second_num


# Best Solution
class Solution(object):
    def fib(self, n):
    	a, b = 0, 1
    	for i in range(n):
            a, b = b, a + b
    	return a



# Question 1 (Easy) Link: https://leetcode.com/problems/two-sum/
class Solution(object):
    def tribonacci(self, n):
        if n < 3:
            if (n == 0):
                return 0
            else:
                return 1
        t_first, t_second, t_third = 0, 1, 1
        for i in range(n - 2):
            t_first, t_second, t_third = t_second, t_third, t_first + t_second + t_third

        return t_third

# Question 217 (Easy) Link: https://leetcode.com/problems/contains-duplicate/
class Solution(object):
    def containsDuplicate(self, nums):
        if ((len(nums) - len(set(nums))) == 0):
            return False
        return True

# Question 53 (Easy) Link: https://leetcode.com/problems/maximum-subarray/
class Solution(object):
    def maxSubArray(self, nums):
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum

# Question 53 (Easy) Link: https://leetcode.com/problems/maximum-subarray/
class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}

        for i in range(len(nums)):
            hash_map[i] = target - nums[i]

        for num in range(len(hash_map)):
            if hash_map[num]in nums:
                num_index = nums.index(hash_map[num])
                if num != num_index:
                    return [num, nums.index(hash_map[num])]

# Another Solution
class Solution(object):
    def twoSum(self, nums, target):
        for i, value in enumerate(nums):
            remaining = (target - value)
            if (remaining in nums):
                pos = nums.index(remaining)
                if (pos != i):
                    return [i, pos]


# Best Solution

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, value in enumerate(nums):

            remaining = (target - value)

            if (remaining in seen):
                return [i, seen[remaining]]
            else:
                seen[value] = i

# Question 70 (Easy) Link: https://leetcode.com/problems/climbing-stairs/
class Solution(object):
    def climbStairs(self, n):
        one_step_ay = 1
        two_step_ay = 2

        if (n == 1):
            return 1

        if (n == 2):
            return 2

        for i in range(n - 2):
            two_step_ay, one_step_ay = one_step_ay + two_step_ay, two_step_ay

        return two_step_ay

class Solution(object):
    def maxSubArray(self, nums):
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum

class Solution(object):
    def maxSubArray(self, nums):
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum


class Solution(object):
    def containsDuplicate(self, nums):
        if ((len(nums) - len(set(nums))) == 0):
            return False
        return True

class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}

        for i in range(len(nums)):
            hash_map[i] = target - nums[i]

        for num in range(len(hash_map)):
            if hash_map[num]in nums:
                num_index = nums.index(hash_map[num])
                if num != num_index:
                    return [num, nums.index(hash_map[num])]
