"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

import statistics

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        sortedNum = sorted(numbers)
        lengthList = int(len(sortedNum))
        if (lengthList % 2) != 0:
            indexMedian = int((lengthList - 1) / 2)
            median = sortedNum[indexMedian]
        else:
            indexMedianUpper = int(lengthList / 2)
            indexMedianLower = indexMedianUpper - 1
            median = statistics.mean([sortedNum[indexMedianUpper],sortedNum[indexMedianLower]])
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
#print(sortedNum)
print(f"This is the median: {median}")
