#<--------------------------- LinkedList Cycle (easy) --------------------------->#

# Grokking Passed
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def has_cycle(head):
  fast, slow = head, head
  while(fast is not None and fast.next is not None):
    fast = fast.next.next
    slow = slow.next

    if fast == slow:
      return True
  return False


# Leetcode Question 141: https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while(fast is not None and fast.next is not None):
            if pos == -1:
                return False
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True

        return False


#<--------------------------- Start of LinkedList Cycle (medium) --------------------------->#

# Grokking Passed
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def find_cycle_start(head):
  p1, p2 = head, head
  # p1 is the fast pointer
  while(p1 is not None and p1.next is not None):
    p1 = p1.next.next
    p2 = p2.next
    if p1 == p2:
      break

  # When the starting pointer matches the fast pointer you have hit the starting node of the cycle
  p2 = head
  while(p1 != p2):
    p1 = p1.next
    p2 = p2.next
  return p1


# Leetcode Question 142: https://leetcode.com/problems/linked-list-cycle-ii/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = head, head
        # p1 is the fast pointer
        while(p1 is not None and p1.next is not None):
            p1 = p1.next.next
            p2 = p2.next
            if p1 == p2:
                break

        else: return None
        # When the starting pointer matches the fast pointer you have hit the starting node of the cycle
        while(p1 != head):
            p1 = p1.next
            head = head.next

        return head


#<--------------------------- Happy Number (medium) --------------------------->#

# Grokking Passed
def sumSquareDigit(num):
  curSum = 0

  for digit in str(num):
    curSum += int(digit) ** 2

  return curSum

def find_happy_number(num):
  fastNum = num # Fast num goes twice as fast
  slowNum = num

  while(fastNum != 1):
    fastNum = sumSquareDigit(sumSquareDigit(fastNum)) # Fast num goes twice as fast
    slowNum = sumSquareDigit(slowNum)

    # print(fastNum, slowNum)
    if fastNum == slowNum and slowNum != 1:
      return False

  return True


# Leetcode Question 202: https://leetcode.com/problems/happy-number/
def sumSquareDigit(num):
    curSum = 0

    for digit in str(num):
        curSum += int(digit) ** 2

    return curSum

class Solution:
    def isHappy(self, n: int) -> bool:
        slowNum = fastNum = n # Fast num goes twice as fast

        while(fastNum != 1):
            fastNum = sumSquareDigit(sumSquareDigit(fastNum)) # Fast num goes twice as fast
            slowNum = sumSquareDigit(slowNum)

            if fastNum == slowNum and slowNum != 1:
                return False

        return True


#<--------------------------- Middle of the LinkedList (easy) --------------------------->#

# Grokking Passed
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def find_middle_of_linked_list(head):
  fast, slow = head, head

  while(fast is not None and fast.next is not None):
    fast = fast.next.next
    slow = slow.next

  return slow


# Leetcode Question 202: https://leetcode.com/problems/happy-number/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
      fast, slow = head, head

      while(fast is not None and fast.next is not None):
        fast = fast.next.next
        slow = slow.next

      return slow
