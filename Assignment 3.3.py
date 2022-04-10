# Assignment 3.3
# Write a Python function to get the maximum and minimum value in a dictionary. Return max and min 
# as a tuple. Ignore any values that are not integers.
# function: def min_max (d1: Dict) -> Tuple:
# IN: {'foo':9, 'bar': 'xyz', 'baz':8, 'boz':4}
# OUT: (9, 4)


def min_max (d1: dict) -> tuple:

    collection = list(d1.values())
    intValues = []

    for values in collection:
        if type(values) == int:
            intValues.append(values)
        maxVal = max(intValues)
        minVal = min(intValues)

    tupMinMax = (maxVal, minVal)

    return tupMinMax

userDictionary = {'foo':9, 'bar': 'xyz', 'baz':4, 'boz':8}
print(min_max(userDictionary))