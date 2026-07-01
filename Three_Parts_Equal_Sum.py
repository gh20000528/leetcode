# Example 1:

# Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
# Example 2:

# Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false


def canThreePartsEqualSum(self, arr: List[int]) -> bool:
    total = sum(arr)
    if total % 3 != 0:
        return False
    
    target = total // 3
    current = 0
    count = 0

    for num in arr:
        current += num
        
        if current == target:
            count += 1
            current = 0

    return count >= 3