# You have to check what is the biggest profit you can make. The index corrospends to the days
# and the values to the prices.

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

def stocks_profit(A):
    max_profit = 0
    for i in range(len(A)-1):
        difference = max(A[i:])-A[i]
        max_profit = max(difference, max_profit)
    return max_profit

print(stocks_profit(A))
