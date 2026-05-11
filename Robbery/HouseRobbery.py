class Solution(object):
    def rob(self, moneyInEachHouse):
        if not moneyInEachHouse:
            return 0
            
        maxMoneyTwoHousesAgo = 0
        maxMoneyOneHouseAgo = 0
        
        for currentHouseMoney in moneyInEachHouse:
            robCurrentHouseTotal = currentHouseMoney + maxMoneyTwoHousesAgo
            skipCurrentHouseTotal = maxMoneyOneHouseAgo
            
            currentMaxMoney = max(robCurrentHouseTotal, skipCurrentHouseTotal)
            
            maxMoneyTwoHousesAgo = maxMoneyOneHouseAgo
            maxMoneyOneHouseAgo = currentMaxMoney
            
        return maxMoneyOneHouseAgo