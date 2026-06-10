# 700. Search in a Binary Search Tree
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]


def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
        return None
    
    if root.val == val:
        return root
    # if the value is less than the current node's value, search in the left subtree
    elif val < root.val:
        return self.searchBST(root.left, val)
    # if the value is greater than the current node's value, search in the right subtree
    elif val > root.val:
        return self.searchBST(root.right, val)