# 5. Write a Python function to convert string values of a given dictionary, into integer/float datatypes. 
# Return and display the new dictionary.
# function: def str_to_num (d1: Dict) -> Dict:

# IN: {'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}
# OUT: {'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}

# IN: {'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60'}
# OUT: {'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60}

# dict1 = {'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}
dict1 = {'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60'}

def str_to_num (d1: dict) -> dict:

    for d in d1:
        for value in d:
            if type(d[value]) == str:
                if '.' in d[value]:
                    d[value] = float(d[value])
                else:
                    d[value] = int(d[value])

    return d1
    
print(str_to_num (dict1))

