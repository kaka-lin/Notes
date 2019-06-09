"""Two Pointers

# Time complexity: O(m+n)
# Space complexity: O(1)

# Runtime: 192ms (91.82%)
# Memory Usage: 41.8 MB (67.17%)
"""
from linked_list import ListNode
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    if headA is None or headB is None:
        return None
        
    ptr_a = headA
    ptr_b = headB
        
    while ptr_a is not ptr_b:
        ptr_a = headB if ptr_a is None else ptr_a.next
        ptr_b = headA if ptr_b is None else ptr_b.next
            
    return ptr_a

