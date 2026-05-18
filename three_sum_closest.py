# 16. 3Sum Closest
# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    ans = nums[0] + nums[1] + nums[2]

    if i in reange(len(nums) -2):
        left  = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if abs(total - target) < abs(ans - target):
                ans = total
            
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return total
    
    return ans
