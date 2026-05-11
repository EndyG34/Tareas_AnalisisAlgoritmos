class Solution(object):
    def minCostClimbingStairs(self, costOfEachStep):
        totalSteps = len(costOfEachStep)
        
        totalCostToReachStep = [0] * (totalSteps + 1)
        
        for currentStep in range(2, totalSteps + 1):
            costFromOneStepBelow = totalCostToReachStep[currentStep - 1] + costOfEachStep[currentStep - 1]
            costFromTwoStepsBelow = totalCostToReachStep[currentStep - 2] + costOfEachStep[currentStep - 2]
            
            totalCostToReachStep[currentStep] = min(costFromOneStepBelow, costFromTwoStepsBelow)
            
        return totalCostToReachStep[totalSteps]