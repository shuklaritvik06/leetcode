class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def createNodes(self, nodes: Optional[ListNode]):
        print(nodes)
        start_node = ListNode(nodes[0])
        current_node = start_node
        for i in range(1, len(nodes)):
            current_node.next = ListNode(nodes[i])
            current_node = current_node.next
        return start_node
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        numberOne = ""
        numberTwo = ""
        result = []
        while l1.next is not None:
            numberOne += str(l1.val)
            l1 = l1.next
        while l2.next is not None:
            numberTwo += str(l2.val)
            l2 = l2.next
        numberOne += str(l1.val)
        numberTwo += str(l2.val)
        total_sum = int(numberOne) + int(numberTwo)
        if total_sum == 0:
            return self.createNodes([0])
        while total_sum != 0:
            result.append(total_sum % 10)
            total_sum = total_sum // 10
        return self.createNodes(result)