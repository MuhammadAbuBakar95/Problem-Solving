# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        fast = head
        slow = head
        it = 0
        
        while fast != None:
            fast = fast.next
            it += 1
            if it % 2 == 1:
                continue
            slow = slow.next
            if fast == slow:
                break

        if fast == None:
            return None
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        print fast.val
        return fast
        

def createLL(arr):
    head = ListNode(arr[0])
    curr = head
    for num in arr[1:]:
        curr.next = ListNode(num)
        curr = curr.next
    return head, curr

def printLL(head):
    curr = head
    while curr != None:
        print curr.val,
        curr = curr.next
    print

arr = [3,2,0,-4]
head, tail = createLL(arr)
tail.next = head.next
print Solution().detectCycle(head)
