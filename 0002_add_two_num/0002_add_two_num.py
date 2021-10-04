# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        ans_tail = ans
        carry = 0
                
        while l1 or l2 or carry:
            if l1 is not None:
                v1 = l1.val
                l1 = l1.next
            else:
                v1 = 0
            
            if l2 is not None:
                v2 = l2.val
                l2 = l2.next
            else:
                v2 = 0           

            carry, cur_value = divmod(v1+v2 + carry, 10)    
                      
            ans_tail.next = ListNode(cur_value)
            ans_tail = ans_tail.next                      
            

        return ans.next