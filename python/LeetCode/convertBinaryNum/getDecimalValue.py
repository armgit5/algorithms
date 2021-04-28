# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        # print(head.next.val)
        # print(head.next.next.val)

        num = head.val
        while head.next:
            num = num * 2 + head.next.val
            head = head.next
        return num


l = ListNode(1)
l.next = ListNode(0)
l.next.next = ListNode(1)

s = Solution()
print(s.getDecimalValue(l))


# a = 1
# print(bin(a))
# print(bin(a << 1))
# print(a << 1)
# print(a >> 1)

