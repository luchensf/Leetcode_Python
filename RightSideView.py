from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        rightside = []
        que = deque([root])
        while que:
            size = len(que)
            for i in range(size):
                node = que.popleft()
                if i == size - 1:
                    rightside.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return rightside
    
    