"""THIS CODE IS AN EXAMPLE OF DICTIONARY OBJECTS CREATION AND USAGE.
A DICTIONARY IS A SET OF <KEY, VALUE> PAIRS, WHERE EACH KEY MUST BE AN HASHABLE OBJECT.
"""

aFirst= {}
print("First: ", aFirst)

aSecond= dict()
print("Second: ", aSecond)

aThird= {'a': 1, 'b': 2}
print("Third: ", aThird)

aFourth= dict({'a': 1, 'b': 2})
print("Fourth: ", aFourth)

aFifth= dict(zip(['h', 'i'], [3, 4]))
print("Fifth: ", aFifth)

aSixth= dict(D='!', G='%', H='&', I='&')
print("Sixth: ", aSixth)

print("Get all keys in the sixth dictionary: ", aSixth.keys())

print("Get all values in the sixth dictionary: ", aSixth.values())

print("Get all <key, value> pairs in the sixth dictionary: ", aSixth.items())

print("<\'D\', \'!\'> pair is in the sixth dictionary? ", ('D', '!') in aSixth)

print("<\'F\', \'/\'> pair is in the sixth dictionary? ", ('F', '/') in aSixth)

print("Get value associated to \'D\' key: ", aSixth['D'])

print("Add <F, /> key in the sixth dictionary...")
aSixth['F']= '/'
print(aSixth)

print("Remove a random pair from the sixth dictionary...", aSixth.popitem())

print("Remove pair with \'D\' key from the sixth dictionary...", aSixth.pop('D'))

#print("Remove an item which key does not occur in the sixth dictionary...", aSixth.pop('T'))

print("Get value associated to \'T\' key with get() method...", aSixth.get('T'))

print("Get value associated to \'T\' key with a default value passed to get() method, in case key does not occur...", aSixth.get('T', 'no_occurrence_of_key'))

print("Get value associated to \'D\' key with a default value passed to get() method, in case key does not occur...", aSixth.get('D', 'no_occurrence_of_key'))

print("Get value associated to \'P\' key with a default value passed to setdefault() method, in case key does not occur...", aSixth.setdefault('P', '$'))

print("Try to override the value of the last inserted item...", aSixth.setdefault('P', '£'))

print("Update sixth dictionary with <\'K\', 14> pair...\nStarting version of the sixth dictionary: ", aSixth)
aSixth.update(K=14)
print("Updated sixth dictionary: ", aSixth)