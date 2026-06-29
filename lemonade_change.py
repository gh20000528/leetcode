# Example 1:

# Input: bills = [5,5,5,10,20]
# Output: true
# Explanation: 
# From the first 3 customers, we collect three $5 bills in order.
# From the fourth customer, we collect a $10 bill and give back a $5.
# From the fifth customer, we give a $10 bill and a $5 bill.
# Since all customers got correct change, we output true.


def lemonadeChange(self, bills: List[int]) -> bool:
    five, ten = 0, 0

    for b in bills:
        # 如果客人付 5 元
        if b == 5: 
            five += 1
        # 如果客人付 10 元
        elif b == 10:
            # 沒 5 元可以找
            if five == 0:
                return False 
            ten += 1
            five -= 1
        # 如果客人付 10 元
        elif b == 20:
            # 有 5 元 + 10 元可以找
            if ten >= 1 and five >= 1:
                ten -= 1
                five -= 1
            # 有三個 5 元可以找
            elif five >= 3:
                five -= 3
            else:
                return False
    
    return True