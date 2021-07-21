# https://leetcode.com/problems/swap-nodes-in-pairs/

from typing import List, Set, Tuple, Dict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if head == None or head.next == None:
            return head

        first = head
        second = head.next
        head = second

        while True:
            next = second.next
            second.next = first # swap 1 and 2

            if next == None or next.next == None:
                first.next = next
                break

            first.next = next.next
            first = next
            second = next.next
        return head

    def print(self, head: ListNode):

        curr = head

        while curr:
            print(curr.val)
            curr = curr.next


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)

one.next = two
two.next = three
three.next = four

s = Solution()
s.print(one)
print()
head = s.swapPairs(one)
s.print(head)




