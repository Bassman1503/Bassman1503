from enum import Enum

class TrafficLight(Enum):
    RED= 1
    YELLOW= 2
    GREEN= 3

print("Red light enum value: ", repr(TrafficLight.RED))
print("Green light enum value: ", repr(TrafficLight.YELLOW))
print("Yellow light enum value: ", repr(TrafficLight.GREEN))

print("Iterate over TrafficLight members: ")
print(TrafficLight(1))
print(TrafficLight(2))
print(TrafficLight(3))
print("Type of the enum members: ", type(TrafficLight.GREEN))
print("Check if a member of an enum class is an instance of it: ", isinstance(TrafficLight.RED, TrafficLight))
print("Print each member's name: ")
for lightColor in TrafficLight: # enum supports iteration of its members
    print(lightColor.name)
print("Different form: ")
for lightColor in TrafficLight:
    print(lightColor)

print("Members of an enum class are hashable, so they can be used as keys in dictionaries and as amembers of a set")
print("Intialize a dictionary with TrafficLight members as keys:")
aDict= {}
aDict[TrafficLight.RED]= 1
aDict[TrafficLight.YELLOW]= 2
aDict[TrafficLight.GREEN]= 3
print(aDict.keys())

print("Access enum members by their names: ")
print(TrafficLight['RED'])
print(TrafficLight['YELLOW'])
print(TrafficLight['GREEN'])
member= TrafficLight.RED
print(member.name) # access to member's name property
print(member.value) # access to member's value property

class Shape(Enum):
    SQUARE= 2
    CIRCLE= 4
    ALIAS_FOR_SQUARE= 2

print(Shape.SQUARE)
print(Shape.ALIAS_FOR_SQUARE)
print(Shape(2))        