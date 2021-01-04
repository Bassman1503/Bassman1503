# Local Scope vs Global Scope visibility (variable initialized only in the global scope)
#

def localScope():
    """Shows an example of local scope variable visibility, in which m value is not initialized.   

    Return nothing.  

    Arguments: no arguments.  
    """

    # Print the value of m, declared in the local scope of the function.
    #
    print("Printing m value from local scope: ", m)


#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#

# Initialize the value of m with a random integer number, in the global scope.
#
m= 5

# Print the value of m, declared in the global scope.
#
print("Printing m value from global scope: ", m)

# Call the function previously declared.
#
localScope()