
"""
if profit is -ve => i mean you buying on high value
if profit is+ve => you buying in small value
if profit is max_so_far => you but at smallest till now
"""
def max_profit(prices):
    n = len(prices)
    i = 0
    j = 1
    maxi = 0
    while i < j and j < n-1:
        diff = prices[j] - prices[i]
        if diff < 0:
            i+=1
            j+=1
        else:
            maxi = max(maxi, diff)
            j+=1
    return maxi

prices = [3, 2, 6, 5, 0, 3]
res = max_profit(prices)
print(f'The result is: {res}')