# 5. Write a Python function to convert string values of a given dictionary, into integer/float datatypes. 
# Return and display the new dictionary.
# function: def str_to_num (d1: Dict) -> Dict:

# IN: {'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}
# OUT: {'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}

# IN: {'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60'}
# OUT: {'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60}

dict1 = {'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}
# dict1 = {'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60'}

for d in dict1:
    for value in d:
        if type(d[value]) == str:
            d[value] = int(d[value])
        # if type(d[value])

        # if type(d[value]) == str:
        #     if isinstance(d[value], int):
        #         d[value] = int(d[value])
        #     elif isinstance(d[value], float):
        #         d[value] = float(d[value])
    print (dict1)

# print (type(dict1))
# print (dict1)