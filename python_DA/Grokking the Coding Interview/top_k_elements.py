#<--------------------------- Top 'K' Numbers (easy) --------------------------->#

# Grokking Passed
from heapq import *


def find_k_largest_numbers(nums, k):
    result = []

    for i in range(k):
        heappush(result, nums[i])

    n = len(nums)

    for j in range(k, n):
        if nums[j] > result[0]:
            heappop(result)
            heappush(result, nums[j])

    return result


def main():

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()


#<--------------------------- Kth Smallest Number (easy) --------------------------->#

# Grokking Passed


def find_Kth_smallest_number(nums, k):
    maxHeap = []

    for num in nums[:k]:
        heappush(maxHeap, -num)

    lenNums = len(nums)
    for num in nums[k:lenNums]:
        if -num > maxHeap[0]:
            heappop(maxHeap)
            heappush(maxHeap, -num)

    return -maxHeap[0]


def main():

    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

    # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()


#<--------------------------- Kth Smallest Number (easy) --------------------------->#

# Grokking Passed


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')


def distanceFromOrigin(x, y):
    return ((x ** 2) + (y ** 2)) ** 0.5


def find_closest_points(points, k):
    result = []
    lenPoints = len(points)
    i = 0

    while(i < lenPoints):
        point = points[i]
        distFromOrigin = distanceFromOrigin(point.x, point.y)

        if i < k:
            heappush(result, (-distFromOrigin, point))

        elif -result[0][0] > distFromOrigin:
            heappop(result)
            heappush(result, (-distFromOrigin, point))

        i += 1

    kClosestPoints = []

    for point in result:
        kClosestPoints.append(point[1])
    return kClosestPoints


def main():

    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()


main()


# Leetcode Question 973: https://leetcode.com/problems/k-closest-points-to-origin/
def distanceFromOrigin(x, y):
    return ((x ** 2) + (y ** 2)) ** 0.5


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        lenPoints = len(points)
        i = 0

        while(i < lenPoints):
            point = points[i]
            distFromOrigin = distanceFromOrigin(point[0], point[1])

            if i < k:
                heappush(result, (-distFromOrigin, point))

            elif -result[0][0] > distFromOrigin:
                heappop(result)
                heappush(result, (-distFromOrigin, point))

            i += 1

        kClosestPoints = []

        for point in result:
            kClosestPoints.append(point[1])
        return kClosestPoints


#<--------------------------- Connect Ropes (easy) --------------------------->#

# Grokking Passed


def minimum_cost_to_connect_ropes(ropeLengths):
    minHeap = []
    result = 0

    for rope in ropeLengths:
        heappush(minHeap, rope)

    while (len(minHeap) > 1):
        rope1 = heappop(minHeap)
        rope2 = heappop(minHeap)
        result += rope1 + rope2
        heappush(minHeap, rope1+rope2)

    return result


def main():

    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()


#<--------------------------- Top 'K' Frequent Numbers (medium) --------------------------->#

# Grokking Passed


def find_k_frequent_numbers(nums, k):
    topNumbers = []
    frequencyHashMap = {}

    for num in nums:
        frequencyHashMap[num] = frequencyHashMap.get(num, 0) + 1

    for num in frequencyHashMap:
        heappush(topNumbers, (frequencyHashMap[num], num))
        if len(topNumbers) > k:
            heappop(topNumbers)

    return [x[1] for x in topNumbers]


def main():

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()


# Leetcode Question 347: https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topNumbers = []
        frequencyHashMap = {}

        for num in nums:
            frequencyHashMap[num] = frequencyHashMap.get(num, 0) + 1

        for num in frequencyHashMap:
            heappush(topNumbers, (frequencyHashMap[num], num))
            if len(topNumbers) > k:
                heappop(topNumbers)

        return [x[1] for x in topNumbers]


#<--------------------------- Frequency Sort (medium) --------------------------->#

# Grokking Passed


def sort_character_by_frequency(inputStr):

    frequencyMap = {}
    maxHeap = []
    for char in inputStr:
        frequencyMap[char] = frequencyMap.get(char, 0) + 1

    for char in frequencyMap:
        heappush(maxHeap, (-frequencyMap[char], char))

    curStr = ''

    while maxHeap:
        result = heappop(maxHeap)
        for _ in range(-result[0]):
            curStr += result[1]
    return curStr


def main():

    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()


# Leetcode Question 451: https://leetcode.com/problems/sort-characters-by-frequency/
class Solution:
    def frequencySort(self, s: str) -> str:

        frequencyMap = {}
        maxHeap = []
        for char in s:
            frequencyMap[char] = frequencyMap.get(char, 0) + 1

        for char in frequencyMap:
            heappush(maxHeap, (-frequencyMap[char], char))

        curStr = ''

        while maxHeap:
            result = heappop(maxHeap)
            for _ in range(-result[0]):
                curStr += result[1]
        return curStr


#<--------------------------- Kth Largest Number in a Stream (medium) --------------------------->#

# Grokking Passed


class KthLargestNumberInStream:
    def __init__(self, nums, k):
        self.minHeap = nums
        heapify(self.minHeap)
        self.k = k

        while len(self.minHeap) > k:
            heappop(self.minHeap)

    def add(self, num):
        heappush(self.minHeap, num)

        if len(self.minHeap) > self.k:
            heappop(self.minHeap)

        return self.minHeap[0]


def main():

    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kthLargestNumber.add(6)))
    print("4th largest number is: " + str(kthLargestNumber.add(13)))
    print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()


# Leetcode Question 703: https://leetcode.com/problems/kth-largest-element-in-a-stream/


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        heapify(self.minHeap)
        self.k = k

        while len(self.minHeap) > k:
            heappop(self.minHeap)

    def add(self, val: int) -> int:
        heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heappop(self.minHeap)

        return self.minHeap[0]


#<--------------------------- Kth Largest Number in a Stream (medium) --------------------------->#

# Grokking Passed


def closest_element(arr, X):
    start, end = 0, len(arr)-1

    if arr[start] > X:
        return start

    if arr[end] < X:
        return end

    while end >= start:
        mid = (start + end) // 2
        curNum = arr[mid]
        if curNum == X:
            return mid
        elif curNum > X:
            end = mid - 1
        else:
            start = mid + 1

    if abs(arr[end] - X) > abs(arr[start] - X):
        return start

    return end


def find_closest_elements(arr, k, x):
    result = []  # Min Heap
    index = closest_element(arr, x)
    target_right, target_left = min(index+k, len(arr)-1), max(0, index-k)

    for i in range(target_left, target_right+1):
        heappush(result, (abs(arr[i]-x), arr[i]))

    final_solution = []
    for _ in range(k):
        final_solution.append(heappop(result)[1])

    final_solution.sort()
    return final_solution


def main():
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()


# Leetcode Question 658: https://leetcode.com/problems/find-k-closest-elements/


def closest_element(arr, X):
    start, end = 0, len(arr)-1

    if arr[start] > X:
        return start

    if arr[end] < X:
        return end

    while end >= start:
        mid = (start + end) // 2
        curNum = arr[mid]
        if curNum == X:
            return mid
        elif curNum > X:
            end = mid - 1
        else:
            start = mid + 1

    if abs(arr[end] - X) > abs(arr[start] - X):
        return start

    return end


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        result = []  # Min Heap
        index = closest_element(arr, x)
        target_right, target_left = min(index+k, len(arr)-1), max(0, index-k)

        for i in range(target_left, target_right+1):
            heappush(result, (abs(arr[i]-x), arr[i]))

        final_solution = []
        for _ in range(k):
            final_solution.append(heappop(result)[1])

        final_solution.sort()
        return final_solution


#<--------------------------- Maximum Distinct Elements (medium) --------------------------->#

# Grokking Passed


def find_maximum_distinct_elements(nums, k):
    freqMap = {}
    numHeap = []
    distinct_nums = 0

    if len(nums) <= k:
        return distinct_nums

    for num in nums:
        freqMap[num] = freqMap.get(num, 0) + 1

    for num in freqMap:
        if freqMap[num] > 1:
            heappush(numHeap, (freqMap[num], num))
        else:
            distinct_nums += 1

    while numHeap and k > 0:
        if numHeap[0][0]-1 > k:
            k = 0
            break

        k -= heappop(numHeap)[0]-1
        distinct_nums += 1

    return distinct_nums - k


def main():

    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()


#<--------------------------- Sum of Elements (medium) --------------------------->#

# Grokking Passed


def find_sum_of_elements(nums, k1, k2):
    minHeap = []
    curSum = 0

    for num in nums:
        heappush(minHeap, num)

    for _ in range(k1):
        heappop(minHeap)

    for _ in range(k2-k1-1):
        curSum += heappop(minHeap)
    return curSum


def main():

    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()


#<--------------------------- Rearrange String (hard) --------------------------->#

# Grokking Passed


def rearrange_string(inputStr):
    freqMap = {}
    freqHeap = []  # Max heap

    for char in inputStr:
        freqMap[char] = freqMap.get(char, 0) + 1

    for char in freqMap:
        heappush(freqHeap, [-freqMap[char], char])

    prevChar = [0, None]
    curString = ''

    while freqHeap:
        curChar = heappop(freqHeap)
        curString += curChar[1]
        curChar[0] += 1

        if prevChar[0] != 0:
            heappush(freqHeap, prevChar)
        prevChar = curChar

    if prevChar[0] != 0:
        return ''

    return curString


def main():
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("aapa"))


main()


# Leetcode Question 767: https://leetcode.com/problems/reorganize-string/
class Solution:
    def reorganizeString(self, inputStr: str) -> str:
        freqMap = {}
        freqHeap = []  # Max heap

        for char in inputStr:
            freqMap[char] = freqMap.get(char, 0) + 1

        for char in freqMap:
            heappush(freqHeap, [-freqMap[char], char])

        prevChar = [0, None]
        curString = ''

        while freqHeap:
            curChar = heappop(freqHeap)
            curString += curChar[1]
            curChar[0] += 1

            if prevChar[0] != 0:
                heappush(freqHeap, prevChar)
            prevChar = curChar

        if prevChar[0] != 0:
            return ''

        return curString
