# 98. Validate Binary Search Tree
# Input: root = [2,1,3]
# Output: true
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.


def isValidBST(self, root: Optional[TreeNode]) -> bool:
    arr = []
    # inorder traversal of a BST should be in sorted order
    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        arr.append(node.val)
        dfs(node.right)

    dfs(root)

    # check if the array is in sorted order
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return False

    return True