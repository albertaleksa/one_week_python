"""
Validate Binary Search Tree (Leetcode 98)
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
 - The left subtree of a node contains only nodes with keys less than the node's key.
 - The right subtree of a node contains only nodes with keys greater than the node's key.
 - Both the left and right subtrees must also be binary search trees.
Example 1:
Input: root = [2,1,3]
Output: true
Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1

Solution:
I will use Depth First Search algorithm to traverse tree in order type.
If the result will be a sorted array, then it's a valid BST.
If unsorted - then invalid BST.
We shouldn't store all array of nodes during traverse, it's enough to store (return)
previous node's value and compare it with current node's value.
If previous node's value > current node's value, then return False (invalid BST).

Time complexity - O(n) in worth case when the wrong value will be the last right child
Space complexity - O(h), where h - height of the tree. O(n) - the worst case, when tree is a linked list



The way it works is, it recursively adds the max and mins.
so as it gets deeper the min/max will be root depending on what side the tree goes
solved initially by just checking if the parent node was greater than left and less than right
but this didn't account for a condition where the right side of the tree,
contained a node that had a value less than the root.
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_valid_bst(self, root):
        # begin from root and previous node's value equal to - Infinity
        prev, res = self.traverse_in_order(root, float("-inf"))
        return res

    def traverse_in_order(self, node, prev_node):
        """
        Recursive function to check if current node's value is more than previous or not
        :param node: current node
        :param prev_node: value of previous node
        :return: tuple of value of previous node and result
        (True - is valid BST on current step, False - is invalid BST)
        """
        # go to left child
        if node.left:
            # go to left
            prev_node, res = self.traverse_in_order(node.left, prev_node)
            # check if BST is not valid
            if not res:
                return prev_node, False
        # compare value of current node to previous
        if prev_node < node.val:
            # assign prev value to current
            prev_node = node.val
        else:
            # quit from recursive
            # BST is not valid
            return prev_node, False
        # go to right child
        if node.right:
            # go to right
            prev_node, res = self.traverse_in_order(node.right, prev_node)
            # check if BST is not valid
            if not res:
                return prev_node, False
        # return True if tree is valid on the current step
        return prev_node, True

    def is_valid_bst_iterative(self, root):
        # use queue to store nodes to visit them from left to right level by level (Breadth First Search)
        # queue will store node and his min and max bound what it should according
        queue = deque()
        # put root into the queue, -inf as left edge, +inf - right edge
        queue.append((root, float("-inf"), float("inf")))

        while queue:
            # get first element from queue
            node, min_val, max_val = queue.popleft()
            if node:
                # node less than left edge or more than right
                if min_val >= node.val or node.val >= max_val:
                    # is not valid BST
                    return False
                # go left
                if node.left:
                    # left child must be more than left edge and less than parent's value
                    # add this node into the queue
                    queue.append((node.left, min_val, node.val))
                # go right
                if node.right:
                    # right child must be more than parent's value and less than right edge
                    # add this node into the queue
                    queue.append((node.right, node.val, max_val))
        return True

    def is_valid_bst_bfs_rec(self, root):
        return self.is_valid_bfs(root, float("-inf"), float("inf"))

    def is_valid_bfs(self, root, min_val, max_val):
        # base case
        # if node is not exist
        if not root:
            return True
        # if current node less than min or more than max
        # then tree is not valid BST
        if root.val <= min_val:
            return False
        if root.val >= max_val:
            return False
        # go recursively through the tree
        # and check if every subtree is a valid BST
        # every left child must be more than left edge and less than parent's value
        # every right child must be less than right edge and more than parent's value
        return self.is_valid_bfs(root.left, min_val, root.val) and self.is_valid_bfs(root.right, root.val, max_val)

#           5
#       1      8
#            4  10

# root = [5, 1, 8, null, null, 4, 10]


if __name__ == "__main__":
    node_1 = TreeNode(1)
    node_4 = TreeNode(4)
    node_10 = TreeNode(10)
    node_8 = TreeNode(8, node_4, node_10)
    node_5 = TreeNode(5, node_1, node_8)

    sol = Solution()
    print(sol.is_valid_bst(node_5))
    print(sol.is_valid_bst_iterative(node_5))
    print(sol.is_valid_bst_bfs_rec(node_5))

