"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        clone = []
        original = []
        mapping = {None: None}
        while head:
            original.append(head)
            clone.append(Node(head.val))
            if len(clone) > 1:
                clone[-2].next = clone[-1]
            mapping[head] = clone[-1]
            head = head.next

        for i in range(len(clone)):
            clone[i].random = mapping[original[i].random]
        return clone[0]
