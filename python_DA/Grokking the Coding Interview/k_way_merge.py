#<--------------------------- Merge K Sorted Lists (medium) --------------------------->#

# Grokking Passed
from __future__ import print_function
import math
from heapq import *


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists):
    minHeap = []
    resultHead, resultTail = None, None

    for root in lists:
        if root is not None:
            heappush(minHeap, root)

    while minHeap:

        curNode = heappop(minHeap)

        if not resultHead:
            resultHead = resultTail = curNode

        else:
            resultTail.next = curNode
            resultTail = resultTail.next

        if curNode.next is not None:
            heappush(minHeap, curNode.next)
    return resultHead


def main():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result != None:
        print(str(result.value) + " ", end='')
        result = result.next


main()


# Leetcode Question 23: https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        resultHead, resultTail = None, None

        for i in range(len(lists)):
            root = lists[i]
            if root is not None:
                heappush(minHeap, (root.val, i))

        while minHeap:

            i = heappop(minHeap)[1]
            curNode = lists[i]

            if not resultHead:
                resultHead = resultTail = curNode

            else:
                resultTail.next = curNode
                resultTail = resultTail.next

            if curNode.next is not None:
                heappush(minHeap, (curNode.next.val, i))

            lists[i] = curNode.next
        return resultHead


#<--------------------------- Kth Smallest Number in M Sorted Lists (Medium) --------------------------->#

# Grokking Passed
def find_Kth_smallest(lists, k):
    minHeap = []
    kNum, numsInserted = -1, 0

    for curList in lists:
        heappush(minHeap, (curList[0], 0, curList))

    while numsInserted < k and minHeap:
        curNum, i, curList = heappop(minHeap)
        kNum = curNum
        numsInserted += 1

        if i+1 < len(curList):
            heappush(minHeap, (curList[i+1], i+1, curList))

    return kNum


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()


# Leetcode Question 378: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        kNum, numsInserted = -1, 0

        for curList in matrix:
            heappush(minHeap, (curList[0], 0, curList))

        while numsInserted < k and minHeap:
            curNum, i, curList = heappop(minHeap)
            kNum = curNum
            numsInserted += 1

            if i+1 < len(curList):
                heappush(minHeap, (curList[i+1], i+1, curList))

        return kNum


#<--------------------------- Kth Smallest Number in a Sorted Matrix (Hard) --------------------------->#

# Grokking Passed
def find_Kth_smallest(matrix, k):
    minHeap = []
    number, numsAdded = -1, 0

    for listIndex in range(min(len(matrix), k)):
        heappush(minHeap, (matrix[listIndex][0], 0, matrix[listIndex]))

    while minHeap and numsAdded < k:
        curNum, i, lst = heappop(minHeap)
        number = curNum
        numsAdded += 1

        if i+1 < len(lst):
            heappush(minHeap, (lst[i+1], i+1, lst))

    return number


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()


#<--------------------------- Smallest Number Range (Hard) --------------------------->#

# Grokking Passed
def find_smallest_range(lists):
    minHeap = []
    rangeStart, rangeEnd = 0, math.inf
    curMaxNumber = -math.inf

    for curList in lists:
        heappush(minHeap, (curList[0], 0, curList))
        curMaxNumber = max(curMaxNumber, curList[0])

    while len(minHeap) == len(lists):
        curNum, i, curArr = heappop(minHeap)
        if rangeEnd - rangeStart > curMaxNumber - curNum:
            rangeStart = curNum
            rangeEnd = curMaxNumber

        if 1+i < len(curArr):
            heappush(minHeap, (curArr[i+1], i+1, curArr))
            curMaxNumber = max(curMaxNumber, curArr[i+1])

    return [rangeStart, rangeEnd]


def main():
    print("Smallest range is: " +
          str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()


# Leetcode Question 632: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minHeap = []
        rangeStart, rangeEnd = 0, math.inf
        curMaxNumber = -math.inf

        for curList in nums:
            heappush(minHeap, (curList[0], 0, curList))
            curMaxNumber = max(curMaxNumber, curList[0])

        while len(minHeap) == len(nums):
            curNum, i, curArr = heappop(minHeap)
            if rangeEnd - rangeStart > curMaxNumber - curNum:
                rangeStart = curNum
                rangeEnd = curMaxNumber

            if 1+i < len(curArr):
                heappush(minHeap, (curArr[i+1], i+1, curArr))
                curMaxNumber = max(curMaxNumber, curArr[i+1])

        return [rangeStart, rangeEnd]
