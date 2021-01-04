# In this example a mutable object will be used to show that changing the value 
# of one of its attribute will change the id of the attribute object, but not 
# of the object itself.
#

# Definition of a class to describe some characteristics of a person
#
class Person:
    def __init__(self, age):
        self.age= age

# Initialize an object which describes a specific person
#
aPerson= Person(age= 42)

print("aPerson object id: ", id(aPerson), flush= True)
print("age attribute object id: ", id(aPerson.age), flush= True)

aPerson.age = 43

print("aPerson object id: ", id(aPerson), flush= True)
print("age attribute object id: ", id(aPerson.age), flush= True)