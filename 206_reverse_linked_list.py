from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def reverse(curr, prev):
        if not curr:
            return prev
        else:
            nxt = curr.next
            curr.next = prev
            return reverse(nxt, curr)

    return reverse(head, None)


listNode = ListNode()
listNode1 = ListNode(1)
listNode2 = ListNode(2)

listNode3 = ListNode(3)
listNode = ListNode(4)

listNode.next = listNode1
listNode1.next = listNode2
listNode2.next = listNode3
listNode3.next = listNode

# Time complexity: O(n)
# Space complexity: O(n)
# Use recursive approach to reverse linked list
# nxt stands for next node
# Think it is a two pointer approach
