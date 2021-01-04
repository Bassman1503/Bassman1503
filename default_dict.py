from collections import defaultdict

aDefaultDict= defaultdict(int)
print(aDefaultDict)
print("Age key value: ", aDefaultDict['age'])
print("Reinitializing dictionary to empty...")
aDefaultDict= defaultdict(int)
print(aDefaultDict)
print("Try to modify age key value (age does not exist in the dictionary!)...")
aDefaultDict['age']+= 1
print("Content of the dictionary: ", aDefaultDict)