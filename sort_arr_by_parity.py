# 905. Sort Array By Parity
# Example 1:

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# Example 2:

# Input: nums = [0]
# Output: [0]


def sortArrayByParity(self, nums: List[int]) -> List[int]:
    left = 0
    rigjt = len(nums) - 1

    while left < right:
        if nums[left] % 2!= 0 and nums[right] % 2 == 0:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] % 2 == 0:
            left += 1
        if nums[right] % 2 != 0:
            right -= 1
    return nums