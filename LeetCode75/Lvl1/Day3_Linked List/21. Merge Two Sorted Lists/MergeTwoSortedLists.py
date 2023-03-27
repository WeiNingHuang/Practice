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
    def __init__(self): 
        self.head = None
        self.tail = None
    
    def add_list_item(self, item):
        # make sure item is a proper node  
        if not isinstance(item, ListNode):
            item = ListNode(item)
            
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
            
        self.tail = item
        return

##

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = temp = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return temp.next
##

lst = [1,2,4]
lst2 = [1,3,4]

list1 = SingleLinkedList()
list2 = SingleLinkedList()

for i in lst:
    list1.add_list_item(i)

for j in lst2:
    list2.add_list_item(j)


##

s = Solution()
s.mergeTwoLists(list1, list2)