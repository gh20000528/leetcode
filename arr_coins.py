# 441. Arranging Coins
# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.

def arrangeCoins(self, n: int) -> int:
    row = 1
    while n >= row:
        n -= row
        row += 1
    
    return row - 1