# Assignemnt 3.1
# Write a Python function to concatenate following dictionaries and return a new one. Display 
# the new dictionary outside the function
# Sample Dictionary : 
# dic1={1:10, 2:20} 
# dic2={3:30, 4:40} 
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# function: def merge_dicts (d1: Dict, d2: Dict, d3: Dict) -> Dict:

dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}


def merge_dicts (d1: dict, d2: dict, d3: dict) -> dict:

    newDic = {**d1, **d2, **d3}
    # newDic.update(d1)
    # newDic.update(d2)
    # newDic.update(d3)

    return newDic

print(merge_dicts (dic1, dic2, dic3))
