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
