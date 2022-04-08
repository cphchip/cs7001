# Assignment 3.3
# Write a Python function to get the maximum and minimum value in a dictionary. Return max and min 
# as a tuple. Ignore any values that are not integers.
# function: def min_max (d1: Dict) -> Tuple:
# IN: {'foo':9, 'bar': 'xyz', 'baz':8, 'boz':4}
# OUT: (9, 4)

d1 = {'foo':9, 'bar': 'xyz', 'baz':4, 'boz':8}

collection = d1.values()

maxVal = 0
minVal = 0
trialVal = 0

for values in collection:
    if type(values) == int:
        
        if values > maxVal:
            maxVal = values
        elif values < maxVal:
            minVal = values

print(maxVal)
print(minVal)