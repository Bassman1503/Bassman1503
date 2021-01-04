# Local Scope vs Enclosing Scope vs Global Scope visibility (variable is initilalized in all visibility scope)
#


def enclosingScope():
    """Shows an example of enclosing scope variable visibility.  

    Return nothing.  

    Arguments:
        no arguments.  
    """
    m= 13

    def localScope():
        """Shows an example of enclosing scope variable visibility.  

        Return nothing.  

        Arguments:
            no arguments.  
        """
        # Print the value of m, declared in the local scope of the function. Here, m value is not initialized.
        #
        print("Printing m value from local scope: ", m)

    # Print the value of m, declared in the scope of the enclosing function.
    #
    localScope()
    print("Printing ma value from enclosing scope: ", m)

#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#

# Print the value of m, declared in the global scope.
#
m= 5
print("Printing m value from global scope: ", m)

# Call the enclosing function.
#
enclosingScope()