__author__ = 'freddie'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root is not None:
            temp = root.left
            root.left = root.right
            root.right = temp

            if root.left is not None:
                self.invertTree(root.left)

            if root.right is not None:
                self.invertTree(root.right)

        return root

