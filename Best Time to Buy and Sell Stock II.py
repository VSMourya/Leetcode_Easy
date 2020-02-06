
def maxProfit(prices):

    stack = []
    profit = 0

    for price in prices:
        if not stack:
            stack.append(price)
        else:
            if stack[-1] > price:
                stack[-1] = price
            else:
                profit += price -stack[-1]
                stack[-1] = price

    return profit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))



