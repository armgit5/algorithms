# https://leetcode.com/problems/palindrome-linked-list/
# https://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/
# https://medium.com/dev-genius/linked-list-algorithm-is-it-a-palindrome-for-singly-linked-list-3137291f76c9


# https://www.youtube.com/watch?v=wk4QsvwQwdQ
# https://leetcode.com/problems/palindrome-linked-list/discuss/1168804/Python-or-O(1)-or-Simple-Readable-Code-or-With-Comments

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print(self):
        while self:
            print(self.val)
            self = self.next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        start = head

        # find the middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next # move up 2

        assert slow.val == 2

        end = self.reverse(slow)

        start.print()
        print()
        end.print()
        print()
        head.print()

        while end:
            if end.val != start.val:
                return False
            end = end.next
            start = start.next

        return True

    # return the last node revered
    def reverse(self, node):
        curr = node
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev



s = Solution()
one = ListNode(1)
two = ListNode(2)
three = ListNode(2)
four = ListNode(1)
five = ListNode(1)
one.next = two
two.next = three
three.next = four
# four.next = five

print(s.isPalindrome(one))