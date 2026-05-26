# 349. Intersection of Two Arrays
# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.


def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # set() = [1, 2, 2, 1] -> {1, 2}
    set1 = set(nums1)
    set2 = set(nums2)
    ans = []

    for num in set1:
        if num in set2:
            ans.append(num)

    return ans 