# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def list_to_num(self, head):
        multiplier = 1
        num = 0
        while head != None:
            num += (head.val * multiplier)
            head = head.next
            multiplier *= 10
        return num
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num = self.list_to_num(l1) + self.list_to_num(l2)
        new_start = ListNode(None)
        current = new_start
        if num == 0:
            return ListNode(0)
        while num > 0:
            digit = num % 10
            current.next = ListNode(digit)
            current = current.next
            num = (num - digit) / 10
        return new_start.next