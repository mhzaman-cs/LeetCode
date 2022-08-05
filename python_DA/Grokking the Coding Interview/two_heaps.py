#<--------------------------- Find the Median of a Number Stream (medium) --------------------------->#

# Grokking Passed
import heapq

class MedianOfAStream:
  large, small = [], []

  def insert_num(self, num):
    heapq.heappush(self.small, -num)

    if self.small and self.large and -self.small[0] > self.large[0]:
      heapq.heappush(self.large, -heapq.heappop(self.small))

    while len(self.small) > len(self.large) + 1:
      heapq.heappush(self.large, -heapq.heappop(self.small))

    while len(self.large) > len(self.small) + 1:
      heapq.heappush(self.small, -heapq.heappop(self.large))


  def find_median(self):
    if len(self.large) == len(self.small):
      return (-self.small[0] + self.large[0])/2
    elif len(self.large) > len(self.small):
      return self.large[0]
    else:
      return -self.small[0]


def main():
  medianOfAStream = MedianOfAStream()
  medianOfAStream.insert_num(3)
  medianOfAStream.insert_num(1)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(5)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(4)
  print("The median is: " + str(medianOfAStream.find_median()))


main()


# Leetcode Question 295: https://leetcode.com/problems/find-median-from-data-stream/
class MedianFinder:

    def __init__(self):
      self.large, self.small = [], []

    def addNum(self, num: int) -> None:
      heapq.heappush(self.small, -num)

      if self.small and self.large and -self.small[0] > self.large[0]:
        heapq.heappush(self.large, -heapq.heappop(self.small))

      while len(self.small) > len(self.large) + 1:
        heapq.heappush(self.large, -heapq.heappop(self.small))

      while len(self.large) > len(self.small) + 1:
        heapq.heappush(self.small, -heapq.heappop(self.large))


    def findMedian(self) -> float:
      if len(self.large) == len(self.small):
        return (-self.small[0] + self.large[0])/2
      elif len(self.large) > len(self.small):
        return self.large[0]
      else:
        return -self.small[0]


#<--------------------------- Sliding Window Median (hard) --------------------------->#

# Grokking Passed
import heapq

class SlidingWindowMedian:

  def find_sliding_window_median(self, nums, k):
    result = []
    i = j = 0
    small, large = [], []
    lenNums = len(nums)
    while j < lenNums:
      heapq.heappush(small, -nums[j])
      if small and large and (-small[0] > large[0]):
        heapq.heappush(large, -heapq.heappop(small))

      if len(small) > len(large) + 1:
        heapq.heappush(large, -heapq.heappop(small))

      if len(large) > len(small) + 1:
        heapq.heappush(small, -heapq.heappop(large))

      if j - i + 1 == k:
        if len(small) == len(large):
          result.append((-small[0]+ large[0])/2)
        elif len(small) > len(large):
          result.append(-small[0])
        else:
          result.append(large[0])

        remNum = nums[i]

        if -remNum in small:
          numIndex = small.index(-remNum)
          small[numIndex] = small[-1]
          small.pop()
          if numIndex < len(small):
              heapq._siftup(small, numIndex)
              heapq._siftdown(small, 0, numIndex)

        elif remNum in large:
          numIndex = large.index(remNum)
          large[numIndex] = large[-1]
          large.pop()
          if numIndex < len(large):
              heapq._siftup(large, numIndex)
              heapq._siftdown(large, 0, numIndex)
        i += 1
      j += 1
    return result

def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()


# Leetcode Question 480: https://leetcode.com/problems/sliding-window-median/
import heapq

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
      result = []
      i = j = 0
      small, large = [], []
      lenNums = len(nums)
      while j < lenNums:
        heapq.heappush(small, -nums[j])
        if small and large and (-small[0] > large[0]):
          heapq.heappush(large, -heapq.heappop(small))

        if len(small) > len(large) + 1:
          heapq.heappush(large, -heapq.heappop(small))

        if len(large) > len(small) + 1:
          heapq.heappush(small, -heapq.heappop(large))

        if j - i + 1 == k:
          if len(small) == len(large):
            result.append((-small[0]+ large[0])/2)
          elif len(small) > len(large):
            result.append(-small[0])
          else:
            result.append(large[0])

          remNum = nums[i]

          if -remNum in small:
            numIndex = small.index(-remNum)
            small[numIndex] = small[-1]
            small.pop()
            if numIndex < len(small):
                heapq._siftup(small, numIndex)
                heapq._siftdown(small, 0, numIndex)

          elif remNum in large:
            numIndex = large.index(remNum)
            large[numIndex] = large[-1]
            large.pop()
            if numIndex < len(large):
                heapq._siftup(large, numIndex)
                heapq._siftdown(large, 0, numIndex)
          i += 1
        j += 1
      return result


#<--------------------------- Maximize Capital (hard) --------------------------->#

# Grokking Passed

from heapq import *


def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
  minCapitalHeap = []
  maxProfitHeap = []

  # insert all project capitals to a min-heap
  for i in range(0, len(profits)):
    heappush(minCapitalHeap, (capital[i], i))

  print(minCapitalHeap)
  # let's try to find a total of 'numberOfProjects' best projects
  availableCapital = initialCapital
  for _ in range(numberOfProjects):
    # find all projects that can be selected within the available capital and insert them in a max-heap
    while minCapitalHeap and minCapitalHeap[0][0] <= availableCapital:
      capital, i = heappop(minCapitalHeap)
      heappush(maxProfitHeap, (-profits[i], i))

    # terminate if we are not able to find any project that can be completed within the available capital
    if not maxProfitHeap:
      break

    # select the project with the maximum profit
    availableCapital += -heappop(maxProfitHeap)[0]

  return availableCapital


def main():

  print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
  print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()


# Leetcode Question 502: https://leetcode.com/problems/ipo/
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
      projCapital, projProfits = [], []
      lenProjects = len(capital)


      for i in range(lenProjects):
        heappush(projCapital, (capital[i], i))

      curCapital = w

      for _ in range(k):

        while projCapital and projCapital[0][0] <= curCapital:
          j = heappop(projCapital)[1]
          heappush(projProfits, (-profits[j], j))

        if not projProfits:
          break

        curCapital += -heappop(projProfits)[0]

      return curCapital
