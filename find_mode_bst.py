# 501. Find Mode in Binary Search Tree
# Input: root = [1,null,2,2]
# Output: [2]
# Input: root = [0]
# Output: [0]


def findMode(self, root: Optional[TreeNode]) -> List[int]:
    arr = []
    # inorder traversal of a BST should be in sorted order
    def dfs(node): 
        if node is None:
            return
        dfs(node.left)
        arr.append(node.val)
        dfs(node.right)
    dfs(root)

    # count the frequency of each number in the array
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    max_freq = max(count.values())
    # find the numbers that have the maximum frequency
    result = []

    for num, freq in count.items():
        if freq == max_freq:
            result.append(num)
    
    return result