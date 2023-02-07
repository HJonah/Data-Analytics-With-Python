"""
This file contains the project1 program.
Program outputs entire contents of file. 

Author: Jonah Hart

Default Command-Line Usage:
    
    python project1.py data_file
    
"""

# Global variable assinging keys to wildlife areas
AREAS = {
    0: 'All',
    1: 'Rawah Wilderness Area',
    2: 'Neota Wilderness Area',
    3: 'Comanche Peak Wilderness Area',
    4: 'Cache la Poudre Wilderness Area'
}

# Global variable indicating the variable name (value) associated with the column (key) for the different quantitiative variables
COLUMNS = {
    0: 'Elevation',
    1: 'Aspect',
    2: 'Slope',
    3: 'Horizontal_Distance_To_Hydrology',
    4: 'Vertical_Distance_To_Hydrology',
    5: 'Horizontal_Distance_To_Roadways',
    6: 'Hillshade_9am',
    7: 'Hillshade_Noon',
    8: 'Hillshade_3pm',
    9: 'Horizontal_Distance_To_Fire_Points'
}
  
def main():
    """
    This is the main() function of the program and it helps in directing the start of code execution.  
    
    Parameters
    ----------
    No parameters.

    Returns
    -------
    None
    """
    # Importing argv object from the module sys
    from sys import argv
    
    # Unpacking the variables in argv object
    script_name, data_file = argv 
    
    # Opening the data file
    data_opened=open(data_file)
    
    # For loop for reading in, stripping line endings, and splitting each line
    for line in data_opened:
        data_split=line.strip().split(",")
        print(data_split)
    
if __name__ == "__main__":
    main()