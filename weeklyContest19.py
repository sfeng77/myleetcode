class Solution():
#         Given an integer, return a base 7 representation of it as a String.
#
# Example 1:
#
# Input: 100
# Output: "202"
#
# Example 2:
#
# Input: -7
# Output: "-10"

    def convertTo7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            return '-' + self.convertTo7(-num)
        s = ''
        while(num >= 7):
            s = str(num % 7) + s
            num /= 7
        s = str(num) + s
        return s


#  Given a binary tree, find the left most element in the last row of the tree.
#
# Example 1:
#
# Input:
#
#     2
#    / \
#   1   3
#
# Output:
# 1
#
# Example 2:
#
# Input:
#
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7
#
# Output:
# 7

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


    def findLeftMostNode(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        myrow = -1
        myrowleft = 0
        st = [(root, 0)]
        while(st):
            nd, row = st.pop(0)
            if row > myrow:
                myrowleft = nd.val
                myrow = row
            if nd.left:
                st+=[(nd.left, row + 1)]
            if nd.right:
                st+=[(nd.right, row + 1)]
        return myrowleft

#
# You need to find the largest element in each row of a Binary Tree.
#
# Example:
#
# Input:
#
#           1
#          / \
#         2   3
#        / \   \
#       5   3   9
#
# Output: [1, 3, 9]
#
#


class Solution(object):
    def findValueMostElement(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:    return []
        myrow = -1
        myrowmax = 0
        res = []
        st = [(root, 0)]
        while(st):
            nd, row = st.pop(0)
            if row > myrow:
                res += [myrowmax]
                myrowmax = nd.val
                myrow = row
            else:
                if nd.val > myrowmax:
                    myrowmax = nd.val
            if nd.left:
                st+=[(nd.left, row + 1)]
            if nd.right:
                st+=[(nd.right, row + 1)]
        return myrowmax[1:]

# Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
#
# You need to return the number of important reverse pairs in the given array.
#
# Example1:
#
# Input: [1,3,2,3,1]
# Output: 2
#
# Example2:
#
# Input: [2,4,3,5,1]
# Output: 3
#



    def reversePairs(self, A):
        # Write your code here
        self.tmp = [0] * len(A)
        return self.mergeSort(A, 0, len(A) - 1)

    def mergeSort(self, A, l, r):
        if l >= r:
            return 0

        m = (l + r) >> 1
        ans = self.mergeSort(A, l, m) + self.mergeSort(A, m + 1, r)
        i, j, k = l, m + 1, l
        while i <= m and j <= r:
            if A[i] > 2 * A[j]:
                ans += m - i + 1
            if A[i] > A[j]:
                self.tmp[k] = A[j]
                j += 1
            else:
                self.tmp[k] = A[i]
                i += 1
            k += 1

        while i <= m:
            self.tmp[k] = A[i]
            k += 1
            i += 1
        while j <= r:
            self.tmp[k] = A[j]
            k += 1
            j += 1
        for i in xrange(l, r + 1):
            A[i] = self.tmp[i]

        return ans

    def reversePairs0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:   return 0
        dp = [0] * n
        for i in range(n-2, -1, -1):
            j = i + 1
            dp[i] = 0
            while(j < n and nums[i] != nums[j]):
                if nums[i] > 2 * nums[j]:
                    dp[i] += 1
                j += 1
            if j < n:
                dp[i] += dp[j]
        #    print dp
        return sum(dp)

    def reversePairs1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:   return 0
        pairs = 0
        for i in range(n -1):
            a = nums[i]
            for j in range(i+1, n):
                if a > nums[j] * 2:
                    print i , j
                    pairs += 1
        return pairs

    def reversePairs2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:   return 0
        pairs = 0
        mynums = sorted(zip(nums, range(n)), key = lambda x:x[0])
        for i in range(n -1):
            j = n - 1
            a, myid = mynums[i]
            while(j >= 0 and mynums[j][0] > 2 * a):
                if mynums[j][1] < myid:
                    pairs += 1
                j -= 1
        return pairs
