# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.helper(root, [0])
        return root

    def helper(self, root: TreeNode, l):
        if not root:
            return
        self.helper(root.right, l)
        root.val += l[0]
        l[0] = root.val
        self.helper(root.left, l)


# class Solution:
#     def convertBST(self, root: TreeNode) -> TreeNode:
#         self.helper(root, [0], 0)
#         return root
#
#     def helper(self, root: TreeNode, l, lvl):
#         p = ""
#         for i in range(lvl):
#             p += "   "
#         p += "helper(root: " + ("None" if not root else str(root.val)) + ", l: " + str(l) + ", lvl:" + str(lvl) + ")"
#         print(p)
#         if not root:
#             return
#         self.helper(root.right, l, lvl + 1)
#         root.val += l[0]
#         l[0] = root.val
#         self.helper(root.left, l, lvl + 1)
