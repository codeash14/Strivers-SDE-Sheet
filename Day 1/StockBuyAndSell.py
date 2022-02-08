def maximumProfit(prices):
    mini = float('inf')
    proffit = 0
    for i in prices:
        mini = min(i, mini)
        proffit = max(proffit, i - mini)
    return proffit
