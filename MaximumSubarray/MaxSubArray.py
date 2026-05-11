class Solution(object):
    def maxSubArray(self, numbersList):
        highestSumFoundSoFar = numbersList[0]
        currentRunningSum = 0
        
        for currentNumber in numbersList:
            if currentRunningSum < 0:
                currentRunningSum = 0
                
            currentRunningSum = currentRunningSum + currentNumber
            
            if currentRunningSum > highestSumFoundSoFar:
                highestSumFoundSoFar = currentRunningSum
                
        return highestSumFoundSoFar