# 217. Contains Duplicate
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.

def containsDuplicate(self, nums: List[int]) -> bool:
    nums.sort()

    for i in range(len(nums) -1):
        if nums[i] == nums[i + 1]:
            return True

    return False