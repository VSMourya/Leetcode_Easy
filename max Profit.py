
#leetcode 121

def maxProfit(prices):
    minPrice = float("inf")
    profit = 0

    for i in range(len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
        elif prices[i] - minPrice > profit:
            profit = prices[i] - minPrice

    return profit


prices = [7,1,5,3,6,4]
print(maxProfit(prices))