## lets say we got some array of numbers and a Target
import sys
sys.path.append('../')
import pranavdefinedMethods as pdm

import timeit
def returnPairs(numbers, target):
    matcher = {}
    ansList = []
    for number in numbers:
        if number in matcher:
            ansList.append((target-number, number))
        else:
            matcher[target-number] = 1

    return ansList

print((returnPairs([-5,3,1,6,8], 3)))
