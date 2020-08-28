'''
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # create a new linked list that will hold the merging
        l3 = ListNode()
        #Loop through n-1 elements (zero index) or recurse
        #create a temp node 
        temp = None
        #Check if lists are empty and return the other one
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        #check if data in l1 is smaller or equal to l2 dta
        if l1.val <= l2.val:
            #Assign temp to l1 value
            temp = l1.val
            #check again if l1 value is smaller
            temp.next = self.mergeTwoLists(l1.next,l2)
        else:
            #if list 2 value is greater than l1 value, assigned value to temp
            temp.l2
            #check again if data is greater or equal than l1 and recurse
            temp.next = self.mergeTwoLists(l1, l2.next)
        return temp