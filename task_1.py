def greedy_change(change):
    result = {}
    coins = [25, 50, 10, 5, 2, 1]

    #in case our list of coins is not sorted
    coins.sort(reverse=True)
    
    for i in coins:
        n = change // i
        if n > 0:
            result[i] = n
            change = change - i * n
        
    return result

if __name__ == '__main__':
    print(greedy_change(157))

