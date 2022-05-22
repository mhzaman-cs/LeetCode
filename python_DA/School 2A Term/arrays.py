# Question 4 (Hard) Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        n1 = len(nums1)
        n2 = len(nums2)

        self.xmax = min([n1,n2])

        self.nums1 = nums1
        self.nums2 = nums2
        self.n1 = n1
        self.n2 = n2

        x_result = self.binary_search(-self.xmax, self.xmax, self.criteria)

        return self.pointer_to_median(x_result)

    # simple median calculation. Only used when len(l) <= 4
    def median(self,l):
        sl = sorted(l)
        if len(sl)%2 == 0:
            m1 = len(sl)//2-1
            m2 = m1+1
            return (sl[m1] + sl[m2])/2.0
        else:
            return sl[(len(sl)-1)//2]

    # take a final pointer position, return the median of two arrays
    def pointer_to_median(self, x):
        # if edge is reached
            # if even parity, must be div div
                # if both divs are on edge, we return the average of remaining two
                # if only one is on edge, we return the average of the other div
            # if odd parity, we just want to return the number
                # the number appear in both left and right side, and should be smaller/larger than the right/left side
        # if edge is not reached
            # for num num situation, two nums must be equal so must be correct
            # for div div situation, l takes the closest two
            # for div num or num div, num must be smallest on the right and largest on the left, so equiv to just return num

        leftside, rightside = self.get_if_valid(x)
        l = [max(leftside), min(rightside)]
        result = self.median(l)
        return result

    def get_if_valid(self, x):
        # get all numbers bordering x. Distinguish between left and right side
        p1 = self.corresponder(x, self.n1)
        p2 = self.corresponder(-x, self.n2)
        leftside = []
        rightside = []
        if p1[0] >= 0:
            leftside.append(self.nums1[p1[0]])
        if p1[1] < self.n1:
            rightside.append(self.nums1[p1[1]])
        if p2[0] >= 0:
            leftside.append(self.nums2[p2[0]])
        if p2[1] < self.n2:
            rightside.append(self.nums2[p2[1]])
        return leftside, rightside

    def corresponder(self, x, n):
        # return (leftnum_index, rightnum_index) if x is pointing to a div
        # return (num_index, num_index) if x is pointing to a number
        # turn x from the center into array index
        center = (n-1)//2
        remainder = n%2
        left = -1
        right = -1
        if remainder == 0:
            # center is a div
            if x%2 == 0:
                # pointer is to a div as well
                left, right = (center+x/2, center+x/2+1)
            else:
                # pointer is to a number
                left, right =  (center + (x+1)/2, center + (x+1)/2)
        else:
            # center is a number
            if x%2 == 0:
                # pointer is to a number
                left, right =  (center + x/2, center + x/2)
            else:
                # pointer is to a div
                left, right =  (center + (x-1)/2, center + (x+1)/2)
        left, right = int(left), int(right)
        return (left, right)

    def criteria(self,x):
        # decide when we want to stop the search
        pointer1 = self.corresponder(x, self.n1)
        pointer2 = self.corresponder(-x, self.n2)

        div1 = (pointer1[0] != pointer1[1])
        div2 = (pointer2[0] != pointer2[1])

        # handle reaching the end situations
        if abs(x) == self.xmax:
            # we need to avoid out of index errors

            # Inner side is never out of range. We can only move inwarrd.
            if x > 0:
                if self.nums2[pointer2[1]] < self.nums1[pointer1[0]]:
                    return -1
                else:
                    return 0
            elif x < 0:
                if self.nums1[pointer1[1]] < self.nums2[pointer2[0]]:
                    return 1
                else:
                    return 0
            else:
                # x max is 0. At least one of the lists has length of 0
                return 0

        l1, r1 = self.nums1[pointer1[0]], self.nums1[pointer1[1]]
        l2, r2 = self.nums2[pointer2[0]], self.nums2[pointer2[1]]

        if l2 > r1:
            return 1
        elif l1 > r2:
            return -1
        else:
            return 0

    # binary search in range [left, right] based on criterion. Recursive
    def binary_search(self, left, right, criterion):
        # base case
        if right < left:
            print("ERROR: no x result found")
            return None

        # both sides should be inclusive
        x = (left + right)//2 # go to the left if even num of numbers in range
        bigOrSmall = criterion(x)
        if bigOrSmall == 0:
            # we found it
            return x
        elif bigOrSmall < 0:
            # go to the left
            result = self.binary_search(left, x-1, criterion)
        elif bigOrSmall > 0:
            # go to the right
            result = self.binary_search(x+1, right, criterion)
        else:
            print("ERROR: WHAT THE HELL")

        return result

# div
#      |
# ... 2 4 ...

# num
#     |
# ... 1 3 ...



# Better Solution

def add_arrays(nums1, nums2):
    nums1.extend(nums2)
    final_nums = list(nums1)
    final_nums.sort()
    return final_nums

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final_nums = add_arrays(nums1, nums2)
        length_array = len(final_nums)
        cen_pos = len(final_nums) / 2

        if cen_pos.is_integer():
            print(cen_pos)
            print(final_nums)
            return ((final_nums[int(cen_pos)] + final_nums[int(cen_pos) - 1])/2)
        else:
            print(cen_pos)
            print(final_nums)
            return final_nums[floor(cen_pos)]


# Question 130 (Medium) Link: https://leetcode.com/problems/single-number/


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for num in range(0, len(nums)-1, 2):
            if nums[num] != nums[num +1]:
                return nums[num]
        return nums[-1]



# Question 136 (Hard) Link: https://leetcode.com/problems/surrounded-regions/submissions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        # If board have less than 3 size in any direction: nothing to do, because all cells located on borders
        if n < 3 or m < 3:
            return

        # DFS to look for the next 'O' cell upper, lower, to the right and to the left of current coordinates
        # If 'O' cell is found, recursevly mark this cell as 'R' which is mean REACHED
        def dfs(row: int, col: int) -> None:
            board[row][col] = 'R'
            if row > 0 and board[row - 1][col] == 'O':
                dfs(row - 1, col)
            if row < n - 1 and board[row + 1][col] == 'O':
                dfs(row + 1, col)
            if col > 0 and board[row][col - 1] == 'O':
                dfs(row, col - 1)
            if col < m - 1 and board[row][col + 1] == 'O':
                dfs(row, col + 1)

        # Go and check left and right borders of the board
        for row in range(n):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][m - 1] == 'O':
                dfs(row, m - 1)

        # Same for check up and down borders of the board
        # Since corners (0,0) and (n - 1, m - 1) where checked in previous cycle, skip them in this one
        for col in range(1, m - 1):
            if board[0][col] == 'O':
                dfs(0, col)
            if board[n - 1][col] == 'O':
                dfs(n - 1, col)

        # Follow through the whole board and flip all 'R' cells back into 'O' and all 'O' cell to 'X'
        # since they're unreacheable from the board located 'O' cell if any
        for row in range(n):
            for col in range(m):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'R':
                    board[row][col] = 'O'



# Question 207 (Medium) Link: https://leetcode.com/problems/course-schedule/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength

# Question 421 (Medium) Link: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


# Question 72 (Medium) Link: https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        if not n: return 0

        r, r1, r2 = -1, 0, m-1
        while r1 <= r2:
            mid = (r1+r2) // 2
            if matrix[mid][0] <= target <= matrix[mid][n-1]: r = mid; break
            elif matrix[mid][0] > target: r2 = mid - 1
            else: r1 = mid + 1
        if r == -1: return False

        c1, c2 = 0, n-1
        while c1 <= c2:
            mid = (c1+c2) // 2
            if matrix[r][mid] == target: return True
            elif matrix[r][mid] > target: c2 = mid - 1
            else: c1 = mid + 1
        return False

# Question 88 (Easy) Link: https://leetcode.com/problems/merge-sorted-array/

class Solution(object):
    def romanToInt(self, s):
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number

# Question 13 (Easy) Link: https://leetcode.com/problems/roman-to-integer/

class TrieNode:
    def __init__(self):
        self.children = dict()                        # children nodes
        self.val = 0                                  # end value

class Trie:
    def __init__(self, n):
        self.root = TrieNode()                        # root node
        self.n = n                                    # max length of all numbers

    def add_num(self, num):
        node = self.root
        for shift in range(self.n, -1, -1):           # only shift self.n bits
            val = 1 if num & (1 << shift) else 0      # verify bit from left to right
            if val not in node.children:
                node.children[val] = TrieNode()
            node = node.children[val]
        node.val = num

class Solution:
    def findMaximumXOR(self, nums):
        max_len = len(bin(max(nums))) - 2             # get max length of all numbers' binary
        trie = Trie(max_len)
        for num in nums: trie.add_num(num)            # build trie

        ans = 0
        for num in nums:                              # for each num, find the number which can create max value with num using XOR
            node = trie.root
            for shift in range(max_len, -1, -1):
                val = 1 if num & (1 << shift) else 0  # verify bit from left to right
                node = node.children[1-val] if 1-val in node.children else node.children[val] # try opposite bit first, otherwise use same bit
            ans = max(ans, num ^ node.val)            # maintain maximum
        return ans

# Question 13 (Easy) Link: https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]




class Solution(object):
    def firstMissingPositive(self, nums):
        for i in xrange(len(nums)):
            while 0 <= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
                tmp = nums[i]-1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in xrange(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1

    # O(nlgn) time
    def firstMissingPositive(self, nums):
        nums.sort()
        res = 1
        for num in nums:
            if num == res:
                res += 1
        return res

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]
