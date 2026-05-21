# 414. Third Maximum Number
# Example 1:

# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
# Example 2:

# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.

def thirdMax(self, nums: List[int]) -> int:
    nums.sort()
    count = 1
    # Iterate through the sorted list in reverse order and count distinct maximums
    for i in range(len(nums) - 2, -1, -1):
        # If the current number is different from the next one, it means we have found a distinct maximum
        if nums[i] != nums[i + 1]:
            count += 1
        # If we have found the third distinct maximum, return it
        if count == 3:
            return nums[i]
    return nums[-1]