'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
'''
 # keep track of the digist on each list
        result = LisNode(0)
        result_tail = result
        carry = 0
        #loop throug the lists:
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2+carry, 10)

            result_tail.next = LisNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        return result.next
'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addTwoNumbers(self, l1, l2 ,c = 0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10 ) 
        
        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next,l2.next,c)
        return ret
      

l1 = [2,4,3]
l2 = [5,6,4]
l = ListNode()
print(l.addTwoNumbers(l1,l2))
# addTwoNumbers(l1,l2)