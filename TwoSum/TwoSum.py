class Solution(object):
    def twoSum(self, listOfNumbers, targetNumber):
        totalNumbers = len(listOfNumbers)
        
        for firstIndex in range(totalNumbers):
            for secondIndex in range(firstIndex + 1, totalNumbers):
                
                currentSum = listOfNumbers[firstIndex] + listOfNumbers[secondIndex]
                
                if currentSum == targetNumber:
                    return [firstIndex, secondIndex]