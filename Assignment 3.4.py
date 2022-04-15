# Assignment 3.4
# Write a Python function to replace dictionary values with their average. Display the dict outside the 
# function.
# IN: {'foo':10, 'bar': 'xyz', 'baz':20, 'boz':30}
# OUT: {'foo':20, 'bar': 'xyz', 'baz':20, 'boz':20}
# function: def avg (d1: Dict) -> None:

from statistics import mean


userDict = {'foo':10, 'bar': 'xyz', 'baz':20, 'boz':30}

def avg (d1: dict) -> None:

    intValues = []
    valueList = list(d1.values())

    for v in valueList:
        if type(v) == int:
            intValues.append(v)
    
    averageValue = mean(intValues)

    for values in d1:
        if type(d1[values]) == int:
            d1[values] = averageValue

    print (d1)

    return

avg(userDict)


