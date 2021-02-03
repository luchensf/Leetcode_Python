import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def trimBST(root: TreeNode, low: int, high: int) -> TreeNode:
    if not root:
        return root
    if root.val < low:
        return trimBST(root.right, low, high)
    if root.val > high:
        return trimBST(root.left, low, high)
    root.left = trimBST(root.left, low, high)
    # print(root.left)
    root.right = trimBST(root.right, low, high)
    # print(root.right)
    return root


def deserialize(input: str) -> TreeNode:
    parts = input.split(',')
    if parts[0] == 'null':
        return None
    root = TreeNode(int(parts[0]))
    deque = collections.deque([root])
    i = 1
    while i < len(parts) and len(deque) > 0:
        cur = deque.popleft()
        if parts[i] != 'null':
            cur.left = TreeNode(int(parts[i]))
            deque.append(cur.left)
        if i + 1 < len(parts) and parts[i + 1] != 'null':
            cur.right = TreeNode(int(parts[i + 1]))
            deque.append(cur.right)
        i += 2
    return root


def ptree(root: TreeNode):
    if not root:
        print('[null]')
    deque = collections.deque([root])
    output = [str(root.val)]
    while len(deque) != 0:
        cur = deque.popleft()
        if len(deque) == 0 and not cur.left and not cur.right:
            break
        if cur.left is not None:
            output.append(str(cur.left.val))
            deque.append(cur.left)
        else:
            output.append('null')

        if cur.right is not None:
            output.append(str(cur.right.val))
            deque.append(cur.right)
        else:
            output.append('null')
    print('[' + ','.join(output) + ']')


# ptree(deserialize('3,0,4,null,2,null,null,1'))
# ptree(deserialize('1,null,2'))


ptree(trimBST(deserialize('3,0,4,null,2,null,null,1'), 1, 3))
