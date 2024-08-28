class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = self.size(head)
        if size == 1:
            return None
        if size == n:
            head = head.next
            return head
        index = size - n
        counter = 0
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy.next
        while counter < index-1:
            curr = curr.next
            counter += 1
        curr.next = curr.next.next
        return dummy.next

    def size(self, head):
        temp = head
        count = 0
        while temp is not None:
            temp = temp.next
            count += 1
        return count