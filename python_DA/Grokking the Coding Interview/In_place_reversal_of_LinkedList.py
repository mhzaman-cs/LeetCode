#<--------------------------- Reverse a LinkedList (easy)  --------------------------->#

# Grokking Passed
from __future__ import print_function

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse(head):
  previous, current = None, head

  while current is not None:
    nextNode = current.next
    current.next = previous
    previous = current
    current = nextNode

  return previous


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse(head)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()

# Leetcode Question 141: https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head

        while current is not None:
          nextNode = current.next
          current.next = previous
          previous = current
          current = nextNode

        return previous


#<--------------------------- Reverse a Sub-list (medium)  --------------------------->#

# Grokking Passed
from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse_sub_list(head, p, q):
  if p >= q:
    return head

  dummy = Node(0, head)

  cur, leftPrev = head, dummy

  for i in range(p-1):
    cur, leftprev = cur.next, cur

  midPrev = None
  for i in range(q-p+1):
    tempNext = cur.next
    cur.next = midPrev
    midPrev, cur = cur, tempNext

  leftprev.next.next = cur
  leftprev.next = midPrev

  return leftprev


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()


# Leetcode Question 92: https://leetcode.com/problems/reverse-linked-list-ii/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
      if left >= right:
        return head

      dummy = ListNode(0, head)

      cur, leftPrev = head, dummy

      for i in range(left-1):
        cur, leftPrev = cur.next, cur

      midPrev = None
      for i in range(right-left+1):
        tempNext = cur.next
        cur.next = midPrev
        midPrev, cur = cur, tempNext

      leftPrev.next.next = cur
      leftPrev.next = midPrev

      return dummy.next



#<--------------------------- Reverse every K-element Sub-list (medium)  --------------------------->#

# Grokking Passed
from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse_every_k_elements(head, k):
  prev, cur = None, head
  i = 0
  dummy = Node(0, head)
  startPrev = dummy

  while(cur is not None):
    if i%k == 0 and i!=0:
      tempNextPrev = startPrev.next
      startPrev.next.next = cur
      startPrev.next = prev
      startPrev = tempNextPrev

    tempNext = cur.next
    cur.next = prev
    cur, prev = tempNext, cur
    i += 1

  startPrev.next.next = None
  startPrev.next = prev


  return dummy.next


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_every_k_elements(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()


# Leetcode Question 25: https://leetcode.com/problems/reverse-nodes-in-k-group/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getKthNode(head, k):
  while head and k > 0:
    head = head.next
    k -=1
  return head


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:


      dummy = ListNode(0, head)
      groupPrev = dummy

      while True:
        kth = getKthNode(groupPrev, k)
        if not kth:
          break

        groupNext = kth.next

        prev, curr = kth.next, groupPrev.next

        while curr != groupNext:
          tempNode = curr.next
          curr.next = prev
          prev, curr = curr, tempNode

        tmpNode = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmpNode

      return dummy.next
