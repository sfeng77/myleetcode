class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n = len(nums)
        if n == 0:
            return None
        m = n / 2
        node = TreeNode(nums[m])
        node.left = self.sortedArrayToBST(nums[:m])
        node.right = self.sortedArrayToBST(nums[m+1:])
        return node
