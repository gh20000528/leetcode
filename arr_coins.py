# 441. Arranging Coins
# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.

def arrangeCoins(self, n: int) -> int:
    row = 1
    # n = 5, row = 1 -> n = 4, row = 2 -> n = 2, row = 3 -> n = -1, row = 4
    while n >= row:
        n -= row
        row += 1
    
    return row - 1