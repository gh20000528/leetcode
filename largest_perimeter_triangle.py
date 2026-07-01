# Example 1:

# Input: nums = [2,1,2]
# Output: 5
# Explanation: You can form a triangle with three side lengths: 1, 2, and 2.


def largestPerimeter(self, nums: List[int]) -> int:
    nums.sort()
    # 從後往前找
    for i in range(len(nums) - 1, 1, -1):
        a = nums[i - 2]
        b = nums[i - 1]
        c = nums[i]
        
        if a + b > c:
            return a + b + c
    return 0