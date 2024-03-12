def  find_min_coins(change):

    coins = [1, 2, 5, 10, 25, 50]

    # initiate the dynamic programming table
    dp = [float('inf')] * (change + 1)
    dp[0] = 0

    #finding and updating minimum amount of coins for change(targeted sum)
    for coin in coins:
        for amount in range(coin, change + 1):
            dp[amount] = min(dp[amount], 1 + dp[amount - coin])
    
    #we would've finished here if needed just the amount of coins
    #return dp[amount] if dp[amount] != amount+1 else -1

    result = {}
    remaining_change = change

    
    for coin in coins:
        #here we are checking if enough change left and if it is minimum of coins for giving change
        while remaining_change >= coin and dp[remaining_change] == 1 + dp[remaining_change - coin]:
            result[coin] = result.get(coin, 0) + 1
            remaining_change -= coin

    return result

if __name__ == '__main__':
    print(find_min_coins(113))

