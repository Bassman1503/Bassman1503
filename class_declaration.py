# This is an example of the declaration of a class in Python 3.x.
# The class represents the concept of a bike.  
#

# Declaration statement of the "Bike" class.  
#
class Bike:

    # Definition of the initializer of a Bike's object.
    #
    def __init__(self, colour, frame_material):
        self.colour= colour
        self.frame_material= frame_material

    # Definition of the method that describes the braking action of a bike.
    #
    def braking(self):
        print("Bike's braking!")


# Instantiate two Bike objects. An object is the Python's
# abstraction for data. 
#
bike_1= Bike('red', 'carbon')
bike_2= Bike('blue', 'aluminium')

# Print attributes of the two Bike objects.
#
print("Colour of the first bike: ", bike_1.colour)
print("Colour of the second bike: ", bike_2.colour)
print("Frame material of the first bike: ", bike_1.frame_material)
print("Frame material of the second bike: ", bike_2.frame_material)

# Call to the "braking" method of the two Bike objects.
# Notice the "." (dot) operator to access the object's 
# scope to retrieve and read its attributes.
#
bike_1.braking()
bike_2.braking()