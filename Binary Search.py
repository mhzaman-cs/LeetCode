#
# Binary Search Leetcode 01/01/2022
#

# Question 704 (Easy) Link: https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1


# Question 34 (Medium) Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

def find_left_most(nums, target, mid):
    while nums[mid] == target:
        if mid > 0:
            mid = mid - 1
        else:
            return mid
    return mid + 1

def find_right_most(nums, target, mid):
    while nums[mid] == target:
        if mid < (len(nums)-1):
            mid = mid + 1
        else:
            return mid
    return mid -1


def first_pos(nums, target):
    left = 0
    right = len(nums) -1

    while left <= right:
        mid = left + (right-left)//2
        if nums[mid] > target:
            right = mid - 1
        if nums[mid] < target:
            left = mid + 1
        elif (nums[mid] == target) & (len(nums) >= 3):
            return find_left_most(nums, target, mid)
        elif (nums[mid] == target) & (len(nums) == 1):
            return 0
        elif (nums[mid] == target) & (len(nums) == 2):
            if nums[0] == target:
                return 0
            else:
                return 1
    return -1

def last_pos(nums, target):
    left = 0
    right = len(nums) -1

    while left <= right:
        mid = left + (right-left)//2
        if nums[mid] > target:
            right = mid - 1
        if nums[mid] < target:
            left = mid + 1
        elif (nums[mid] == target) & (len(nums) >= 3):
            return find_right_most(nums, target, mid)
        elif (nums[mid] == target) & (len(nums) == 1):
            return 0
        elif (nums[mid] == target) & (len(nums) == 2):
            if nums[1] == target:
                return 1
            else:
                return 0
    return -1


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [first_pos(nums, target), last_pos(nums, target)]
