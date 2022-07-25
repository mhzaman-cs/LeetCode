#<--------------------------- Merge Intervals (medium) --------------------------->#

# Grokking Passed
from __future__ import print_function

class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
  intLen = len(intervals)
  if len(intervals) < 2:
    return intervals

  intervals.sort(key=lambda x: x.start)

  merged = []

  start = intervals[0].start
  end = intervals[0].end

  for i in range(1, intLen):
    curInt = intervals[i]

    if curInt.start < end:
      end = max(curInt.end, end)

    else:
      merged.append(Interval(start, end))
      start = curInt.start
      end = curInt.end

  merged.append(Interval(start, end))
  return merged


def main():
  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    i.print_interval()
  print()

main()


# Leetcode Question 56: https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      lenInt = len(intervals)

      if lenInt < 2:
        return intervals

      mergedIntervals = []
      intervals.sort(key=lambda x: x[0])


      start = intervals[0][0]
      end = intervals[0][1]

      for i in range(1, lenInt):
        interval = intervals[i]
        if end >= interval[0]:
          end = max(end, interval[1])

        else:
          mergedIntervals.append([start, end])
          start = interval[0]
          end = interval[1]

      mergedIntervals.append([start, end])
      return mergedIntervals


#<--------------------------- Insert Interval (medium) --------------------------->#

# Grokking Passed
def insert(intervals, new_interval):
  merged = []
  start = new_interval[0]
  end = new_interval[1]
  notAppeneded = True

  for i in intervals:
    curIStart = i[0]
    curIEnd = i[1]

    if notAppeneded and ((start >= curIStart and start <= curIEnd) or (end >= curIStart and end <= curIEnd) or (curIStart >= start and curIEnd <= end) or (curIStart <= start and curIEnd >= end)):
      start = min(curIStart, start)
      end = max(curIEnd, end)
    elif notAppeneded and i[0] > end:
      merged.append([start, end])
      merged.append(i)
      notAppeneded = False
    else:
      merged.append(i)

  if notAppeneded:
    merged.append([start, end])

  return merged


def main():
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()


# Leetcode Question 57: https://leetcode.com/problems/insert-interval/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
      merged = []
      start = newInterval[0]
      end = newInterval[1]
      notAppeneded = True

      for i in intervals:
        curIStart = i[0]
        curIEnd = i[1]

        if notAppeneded and ((start >= curIStart and start <= curIEnd) or (end >= curIStart and end <= curIEnd) or (curIStart >= start and curIEnd <= end) or (curIStart <= start and curIEnd >= end)):
          start = min(curIStart, start)
          end = max(curIEnd, end)
        elif notAppeneded and i[0] > end:
          merged.append([start, end])
          merged.append(i)
          notAppeneded = False
        else:
          merged.append(i)

      if notAppeneded:
        merged.append([start, end])

      return merged


#<--------------------------- Intervals Intersection (medium) --------------------------->#

# Grokking Passed
def merge(intervals_a, intervals_b):
  result = []
  iA, iB = 0, 0
  lenA, lenB = len(intervals_a), len(intervals_b)

  while(iA < lenA and iB < lenB):
    aInt, bInt = intervals_a[iA], intervals_b[iB]
    BoverlapsA = bInt[0] >= aInt[0] and bInt[0] <= aInt[1]
    AoverlapsB = aInt[0] >= bInt[0] and aInt[0] <= bInt[1]

    if BoverlapsA or AoverlapsB:
      result.append([max(bInt[0], aInt[0]), min(bInt[1], aInt[1])])
    if aInt[1] < bInt[1]:
      iA += 1
    else:
      iB += 1
  return result


def main():
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))

main()


# Leetcode Question 986: https://leetcode.com/problems/interval-list-intersections/
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
      result = []
      iA, iB = 0, 0
      lenA, lenB = len(firstList), len(secondList)

      while(iA < lenA and iB < lenB):
        aInt, bInt = firstList[iA], secondList[iB]
        BoverlapsA = bInt[0] >= aInt[0] and bInt[0] <= aInt[1]
        AoverlapsB = aInt[0] >= bInt[0] and aInt[0] <= bInt[1]

        if BoverlapsA or AoverlapsB:
          result.append([max(bInt[0], aInt[0]), min(bInt[1], aInt[1])])
        if aInt[1] < bInt[1]:
          iA += 1
        else:
          iB += 1
      return result


#<--------------------------- Conflicting Appointments (medium) --------------------------->#

# Grokking Passed
def can_attend_all_appointments(intervals):
  intervals.sort(key=lambda x:x[0])
  i = 0
  lenInt = len(intervals)

  while(i < lenInt-1):
    if intervals[i][1] > intervals[i+1][0]:
      return False
    i += 1
  return True


def main():
  print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
  print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
  print("Can attend all appointments: " + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()
