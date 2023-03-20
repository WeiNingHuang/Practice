"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""

##
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SingleLinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        if not self.head:
            self.head = ListNode(data)
            return
        
        current = self.head
        
        while current.next:
            current = current.next
        current.next = ListNode(data)


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass
##

ll = SingleLinkedList()

a = [1,2,3,4]

for i in a:
    ll.append(i)

cur = ll.head

##
while cur:
    print(cur.val, end='->')
    cur = cur.next
