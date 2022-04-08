# Assignment 3.2
# Write a Python function to check whether a given key already exists in a dictionary. 
# function: def isKey (d1: Dict, key: Any) -> Boolean:

dict1 = {'goose': 'egg', 2:'chicken'}

def isKey (d1: dict, key: any) -> bool:

    if key in d1:
        return True
    else:
        return False

print(isKey(dict1, 2))