def exchange(price, cash):
    if(cash<=100):
        coins = [0,0,0,0]
        coins[0] = int(price/10)
        dif10= price % 10
        coins[1] = int(dif10/5)
        dif5= dif10 % 5
        coins[2] = int(dif5/2)
        dif2= dif5 % 2
        coins[3] = int(dif2/1)
        return coins
    
    else:
        return coins
    

def logic_coins(coins, existing_coins):
    logic_coins = [0,0,0,0]
    if (existing_coins[0] >= coins[0]):
        logic_coins[0] = coins[0]
    else:
        missing_10 = coins[0] - existing_coins[0]
        extra_5 = missing_10 * 2
        coins [1] = coins [1] + extra_5
        
    
    if (existing_coins[0] >= coins[0]):
        logic_coins[1] = coins[1]
    else:
        missing_5 = coins[1] - existing_coins[1]
        extra_2 = missing_5 * 2
        extra_1 = missing_5
        coins [2] = coins [2] + extra_2
        coins [3] = coins [3] + extra_1
        
    if (coins[2] >= existing_coins[2]):
        logic_coins[2] = coins[2]
    else:
        missing_2 = coins[2] - existing_coins[2]
        extra_1 = missing_2 * 2 
        coins [3] = coins [3] + extra_1
    
    if (coins[3] >= existing_coins[3]):
        logic_coins[3] = coins[3]
    else:
        print("No enough change")
    
   
    return logic_coins
    

existing_coins = [100,100,100,100]
price = 47 
cash = 50
change= exchange(price, cash)
print(change)
coins_change = logic_coins(change, existing_coins)
print(coins_change)