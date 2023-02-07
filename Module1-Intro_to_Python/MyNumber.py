"""
This file contains the MyNumber class.

Author: Stephen Ficklin and Jonah Hart

Default Command-Line Usage:
    
    NONE : Import as module into other python script

"""

class MyNumber:
    """
    This class assigns a number and conducts addition and subtraction mathmatical operations on that number
    
    Attributes
    ----------
    x: int
        The number that is assigned to the class object
    
    Methods
    -------
    validateInt(z):
        Validates if the arguments passed to functions are integers
        If they aren't, an error or exception statement will be printed
    __init__():
        function that assigns an integer value to the class object MyNumber 
    print():
        Prints the number assigned to the class object MyNumber
    add(y):
        Adds the number assigned to y to the number assigned to the class object
    subtract(y):
        Subtracts the number asigned to y from the number assigned to the class object
    main():
        Assigning tests for program/ not needed program code into main() to be ignored when module is used
    """
    
    def validateInt(self,z):
        """
        This function validates whether the arguments used in the program are integers.
        If they aren't integers, the program will output an error and throw an exception.
        If they are integers, function will not execute and it will pass to the next function.
    
        Parameters
        ----------
        z : int
            A supposed integer value that is used during the program.
            This can either be the number assigned to the class object or a number used for mathmetical operations.
       
        Returns
        -------
        None
        """
        
        if not type(z) == int:
            print("Argument cannot be a string, please provide an integer")
            raise Exception("Please provide an integer when using the MyNumber object")
        else:
            pass 
        
    def __init__(self, x):
        """
        This function assigns the attribute x to the class object MyNumber. 
    
        Parameters
        ----------
        x : int
            Number that will be assigned to class object.
        
        Returns
        -------
        None
        """
        
        self.validateInt(x)
        self.x = x
    
    def print(self):
        """
        This function prints the number that is assgined to the class object.
    
        Parameters
        ----------
        self : int
            self is the reserved word that refers to the class object itself. Class object should be integer. 
        
        Returns
        -------
        None
        """
        
        print("The number is: {}".format(self.x))
        
    def add(self, y):
        """
        This function adds the argument y to the number assigned to the class object.
    
        Parameters
        ----------
        y : int
            An integer value that can be used for mathmatical operations with the number assigned to the class object.
        
        Returns
        -------
        None
        """
        
        self.validateInt(y)
        self.x = self.x + y

    def subtract(self, y):
        """
        This function subtracts the argument y from the number assigned to the class object MyNumber.
    
        Parameters
        ----------
        y : int
            An integer value that can be used for mathmatical operations with the number assigned to the class object.
       
        Returns
        -------
        None
        """
        
        self.validateInt(y)
        self.x = self.x - y

def main():
    """
    This is the main() function of the program and it helps in directing the start of code execution.  
    
    Parameters
    ----------
    None
   
    Methods
    -------
    xval:
        Variable that is assigned the integer 3
    yval:
        Variable that is assigned the integer 2
    number:
        Creating a class object of the type MyNumber
    number.print():
        Class function that prints the number assigned to the class object MyNumber
    number.add()
        Class function that adds an integer value to the number assigned to the class object MyNumber
    number.subtract(): 
        Class function that subtracts an integer value from the number assigned to the class object MyNumber

    Returns
    -------
    None
    """
    
    xval = 3
    yval = 2
    number = MyNumber(2)
    number.print()
    number.add(yval)
    number.print()
    number.subtract(yval)
    number.print()

if __name__ == "__main__":
    """
    If statement that if True then runs the below code (main()). Aka, executes the main() function. 
    If False, main() function is skipped. 
    """
    
    main()