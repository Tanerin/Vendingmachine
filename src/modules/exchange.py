class Change_Coins:
    def __init__(self, coins10, coins5, coins2, coins1):
        self. existing_coins =  [coins10,coins5,coins2,coins1]

    def exchange(self, price, cash):
        change = cash - price
        print("Change:"+str(change)) 
        if(change<=100):
            dif10= 0 
            dif5 = 0
            dif2 = 0
            coins = [0,0,0,0]
            if (change/10) >= 1:
                coins[0] = int(change/10)
                dif10 = change % 10
            if (dif10/5) >= 1:
                coins[1] = int(dif10/5)
            dif5= dif10 % 5
            if  (dif5/2) >= 1: 
                coins[2] = int(dif5/2)
            dif2= dif5 % 2
            if  (dif2/1) >= 1:
                coins[3] = int(dif2/1)
            return coins
    
        else:
            return coins
    

    def logic_coins(slef, coins):
        logic_coins = [0,0,0,0]
        if (existing_coins[0] >= coins[0]):
            logic_coins[0] = coins[0]
        else:
            missing_10 = coins[0] - existing_coins[0]
            extra_5 = missing_10 * 2
            coins [1] = coins [1] + extra_5
        
        if (existing_coins[0] >= coins[1]):
            logic_coins[1] = coins[1]
        else:
            missing_5 = coins[1] - existing_coins[1]
            extra_2 = missing_5 * 2
            extra_1 = missing_5
            coins [2] = coins [2] + extra_2
            coins [3] = coins [3] + extra_1
        
        if (existing_coins[0] >= coins[2]):
            logic_coins[2] = coins[2]
        else:
            missing_2 = coins[2] - existing_coins[2]
            extra_1 = missing_2 * 2 
            coins [3] = coins [3] + extra_1
    
        if (existing_coins[0] >= coins[3]):
            logic_coins[3] = coins[3]
        else:
            print("No enough change")
     
        return logic_coins
    
    def pop_coins(self, given_change):
        self.existing_coins
        self.existing_coins[0]= existing_coins[0] - given_change[0]
        self.existing_coins[1]= existing_coins[1] - given_change[1]
        self.existing_coins[2]= existing_coins[2] - given_change[2]
        self.existing_coins[3]= existing_coins[3] - given_change[3] 

    def add_coins(self, string_add):
        self.existing_coins
        self.existing_coins[0]= existing_coins[0] - string_add[0]
        self.existing_coins[1]= existing_coins[1] - string_add[1]
        self.existing_coins[2]= existing_coins[2] - string_add[2]
        self.existing_coins[3]= existing_coins[3] - string_add[3] 
    
