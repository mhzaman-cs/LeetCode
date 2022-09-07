#<--------------------------- 0/1 Knapsack (medium) --------------------------->#

# Grokking Passed
def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    dp = [0 for x in range(capacity+1)]

    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    for c in range(capacity+1):
        if weights[0] <= c:
            dp[c] = weights[0]

    for i in range(1, n):
        for c in range(capacity, -1, -1):
            profit1 = 0

            if weights[i] <= c:
                profit1 = profits[i] + dp[c - weights[i]]

            dp[c] = max(profit1, dp[c])

    return dp[capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()


#<--------------------------- Equal Subset Sum Partition (medium) --------------------------->#

# Grokking Passed
def can_partition(num):
    s = sum(num)
    n = len(num)

    if s % 2 != 0:
        return False

    target_s = int(s/2)

    dp = [[False for _ in range(target_s + 1)] for _ in range(n)]

    # Since every first value requires a vlaue of 0, which can be achived with the empty set
    for i in range(n):
        dp[i][0] = True

    for j in range(1, target_s + 1):
        dp[0][j] = j == num[0]

    for i in range(1, n):
        for j in range(1, target_s+1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i-1][j - num[i]]

    return dp[n-1][target_s]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()


# Leetcode Question 416: https://leetcode.com/problems/partition-equal-subset-sum/
class Solution:
    def canPartition(self, num: List[int]) -> bool:
        s = sum(num)
        n = len(num)

        if s % 2 != 0:
            return False

        target_s = int(s/2)

        dp = [[False for _ in range(target_s + 1)] for _ in range(n)]

        # Since every first value requires a vlaue of 0, which can be achived with the empty set
        for i in range(n):
            dp[i][0] = True

        for j in range(1, target_s + 1):
            dp[0][j] = j == num[0]

        for i in range(1, n):
            for j in range(1, target_s+1):
                if dp[i-1][j]:
                    dp[i][j] = dp[i-1][j]
                elif j >= num[i]:
                    dp[i][j] = dp[i-1][j - num[i]]

        return dp[n-1][target_s]


#<--------------------------- Subset Sum (medium) --------------------------->#

# Grokking Passed
def can_partition(num, curSum):
    n = len(num)

    dp = [[False for _ in range(curSum+1)] for _ in range(n)]

    for j in range(1, curSum + 1):
        dp[0][j] = j == num[0]

    for i in range(n):
        dp[i][0] = True

    for i in range(1, n):
        for j in range(1, curSum+1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i - 1][j - num[i]]

    return dp[n-1][curSum]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()


#<--------------------------- Minimum Subset Sum Difference (hard) --------------------------->#

# Grokking Passed
def can_partition(num):
    n = len(num)
    s = sum(num)
    target_s = int(s/2)

    dp = [[False for _ in range(target_s+1)] for _ in range(n)]

    for j in range(target_s+1):
        dp[0][j] = j == num[0]

    for i in range(n):
        dp[i][0] = True

    for i in range(1, n):
        for j in range(1, target_s+1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]

            elif j >= num[i]:
                dp[i][j] = dp[i-1][j - num[i]]

    for i in range(target_s, -1, -1):
        if dp[-1][i]:
            return abs((s-i)-i)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
