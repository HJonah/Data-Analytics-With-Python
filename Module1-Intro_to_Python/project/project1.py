"""
This file contains the project1 program.
The project1 program contains the Max_Value(), Min_Value(), Average() functions that can be used to calculate the max, min, and average of a specific column in a datafile. 
Also, program contains the functions Wilderness_Max(), Wilderness_Min(), and Wilderness_Average() which can be used to calculate the max, min, and average of the first 10 columns for the four wilderness areas of the covtype.data file.

Author: Jonah Hart

Group: Yes, worked in group with Juliana Pazos

Default Command-Line Usage:
    
    python project1.py data_file
    
"""

from sys import argv # Importing argv object from the sys module

# Global variable assinging keys to wilderness areas
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

def Max_Value(x):
    """
    This function finds and outputs the maximum value for a column in a dataset.
    
    Parameters
    ----------
    x : integer
        Integer representing the column number in a dataset. 

    Returns
    -------
    col_max
        A float value that is the maximum value in the column.
    """
    
    script_name, data_file = argv # Unpacking of argv object (repeated in every function)
    p1_data_file=open(data_file) # Opening of the data file (repeated in every function)
    col_max=0 # Creating col_max variable for function to start comparison that occurs in for loop 
    # For loop to loop through every line of the data file and strip and split the contents of the line into a list
    for line in p1_data_file: 
        p1_data_split=line.strip().split(",")
        # if statement to compare if value selected from list is greater than the number that is already assigned to col_max
        if float(p1_data_split[x]) > col_max:
            col_max=float(p1_data_split[x])
    return col_max
    p1_data_file.close() # Closing of data file (repeated in every function)
    
def Min_Value(x):
    """
    This function finds and outputs the minimum value for a column in a dataset.
    
    Parameters
    ----------
    x : integer
        Integer representing the column number in a dataset. 

    Returns
    -------
    col_min
        A float value that is the minimum value in the column.
    """
    
    script_name, data_file = argv 
    p1_data_file=open(data_file)
    col_min=float('inf') # Creating col_min variable for function to start comparison that occurs in for loop 
     # For loop to loop through every line of the data file and strip and split the contents of the line into a list
    for line in p1_data_file:
        p1_data_split=line.strip().split(",")
        # if statement to compare if value selected in list is less than the number already assigned in col_min
        if float(p1_data_split[x]) < col_min: 
            col_min=float(p1_data_split[x]) 
    return col_min
    p1_data_file.close()

def Average(x):
    """
    This function calculates the average value for a column in a dataset.
    
    Parameters
    ----------
    x : integer
        Integer representing the column number in a dataset. 

    Returns
    -------
    Average
        A float value that is the average value of the column. 
    """
    
    script_name, data_file = argv 
    p1_data_file=open(data_file)
    Sum=0 # Creating variable Sum in which the values in a column will be added to
    Length=0 # Creating variable Length to add 1 to it each time a loop was called (gives number of values in column)
    # For loop to loop through every line of the data file and strip and split the contents of the line into list
    for line in p1_data_file:
        p1_data_split=line.strip().split(",")
        Sum=Sum+float(p1_data_split[x]) # Adding a value at a specific location of the list to the Sum variable
        Length=Length+1 # Adding 1 to the Length variable everytime the loop runs
    Average = Sum/Length # Calculating the average of the column by taking the Sum of the column and dividing it by the Length
    return Average
    p1_data_file.close()

def Wilderness_Max(x):
    """
    This function finds and outputs the maximum value for the different wilderness areas for a specific column. 
    
    Parameters
    ----------
    x : integer
        Integer representing the column number in a dataset. 

    Returns
    -------
    [rawah_max,neota_max,comanche_max,cache_max]
        A list with the maximum value of the x column for each of the four wilderness areas.
    """
    
    script_name, data_file = argv
    p1_data_file=open(data_file)
    # Creating max variables for every wilderness area to start comparisons that occur in the for loop 
    rawah_max=0  
    neota_max=0  
    comanche_max=0 
    cache_max=0 
    
    # For loop to loop through every line of the data file and strip and split the contents of the line into a list
    for line in p1_data_file: 
        p1_data_split=line.strip().split(",")
        # If statements used to seperate the data and comparisons by wilderness area
        # Greater than comparisons made between the specific value in the list and value assigned to area_max variable
        if float(p1_data_split[10]) == 1 and float(p1_data_split[x]) > rawah_max:
            rawah_max=float(p1_data_split[x])
        elif float(p1_data_split[11]) == 1 and float(p1_data_split[x]) > neota_max:
            neota_max=float(p1_data_split[x])
        elif float(p1_data_split[12]) == 1 and float(p1_data_split[x]) > comanche_max:
            comanche_max=float(p1_data_split[x])
        elif float(p1_data_split[13]) == 1 and float(p1_data_split[x]) > cache_max:
            cache_max=float(p1_data_split[x])
   
    return [rawah_max,neota_max,comanche_max,cache_max]
    p1_data_file.close()

def Wilderness_Min(x):
    """
    This function finds and outputs the minimum value for the different wilderness areas for a specific column. 
    
    Parameters
    ----------
    x : integer
        Integer representing the column number in a dataset. 

    Returns
    -------
    [rawah_min,neota_min,comanche_min,cache_min]
        A list with the minimum value of the x column for each of the four wilderness areas.
    """
    
    script_name, data_file = argv
    p1_data_file=open(data_file)
    # Creating min variables for every wilderness area to start comparisons that occur in the for loop 
    rawah_min=float('inf')
    neota_min=float('inf')
    comanche_min=float('inf')
    cache_min=float('inf')
    
    # For loop to loop through every line of the data file and strip and split the contents of the line into a list
    for line in p1_data_file:
        p1_data_split=line.strip().split(",")
        # If statements used to seperate the data and comparisons by wilderness area
        # Less than comparisons made between the specific value in the list and value assigned to area_min variable
        if float(p1_data_split[10]) == 1 and float(p1_data_split[x]) < rawah_min:
            rawah_min=float(p1_data_split[x])
        elif float(p1_data_split[11]) == 1 and float(p1_data_split[x]) < neota_min:
            neota_min=float(p1_data_split[x])
        elif float(p1_data_split[12]) == 1 and float(p1_data_split[x]) < comanche_min:
            comanche_min=float(p1_data_split[x])
        elif float(p1_data_split[13]) == 1 and float(p1_data_split[x]) < cache_min:
            cache_min=float(p1_data_split[x])
   
    return [rawah_min,neota_min,comanche_min,cache_min]
    p1_data_file.close()

def Wilderness_Average(x):
    """
    This function calculates the average value for the different wilderness areas for a specific column. 
    
    Parameters
    ----------
    x : integer
        Integer representing the column number in a dataset. 

    Returns
    -------
    [rawah_average, neota_average, comanche_average, cache_average]
        A list with the average value of the x column for each of the four wilderness areas.
    """
    
    script_name, data_file = argv 
    p1_data_file=open(data_file)
    # Creating dictionary to house the sums of the respective column for each of the wilderness areas
    wilderness_sums = {'Rawah' : 0,
                       'Neota' : 0,
                       'Comanche': 0, 
                       'Cache' : 0,
                      }
    # Creating dictionary to house the lengths (number of values) of the respective column for each of the wilderness areas
    wilderness_lengths = {'Rawah' : 0,
                       'Neota' : 0,
                       'Comanche': 0, 
                       'Cache' : 0,
                      }
    
    # For loop to loop through every line of the data file and strip and split the contents of the line into a list 
    for line in p1_data_file:
        p1_data_split=line.strip().split(",")
        # If statements used to seperate the data and aditions to dictionaries by wilderness area
        # Loop runs through if statements and adds the specific value from the list to the sums dictionary
        # and adds 1 to the lengths dictionary, for the respective wilderness area
        if float(p1_data_split[10]) == 1:
            wilderness_sums['Rawah']= wilderness_sums['Rawah']+float(p1_data_split[x])
            wilderness_lengths['Rawah']= wilderness_lengths['Rawah']+1
        elif float(p1_data_split[11]) == 1:
            wilderness_sums['Neota']=wilderness_sums['Neota']+float(p1_data_split[x])
            wilderness_lengths['Neota']= wilderness_lengths['Neota']+1
        elif float(p1_data_split[12]) == 1:
            wilderness_sums['Comanche']=wilderness_sums['Comanche']+float(p1_data_split[x])
            wilderness_lengths['Comanche']=wilderness_lengths['Comanche']+1
        elif float(p1_data_split[13]) == 1:
            wilderness_sums['Cache']=wilderness_sums['Cache']+float(p1_data_split[x])
            wilderness_lengths['Cache']=wilderness_lengths['Cache']+1
    
    # Calculating the averages by taking the sums of the wilderness areas
    # and dividing it by their respective lengths
    rawah_average = wilderness_sums['Rawah']/wilderness_lengths['Rawah']
    neota_average = wilderness_sums['Neota']/wilderness_lengths['Neota']
    comanche_average = wilderness_sums['Comanche']/wilderness_lengths['Comanche']
    cache_average = wilderness_sums['Cache']/wilderness_lengths['Cache']
   
    return [rawah_average, neota_average, comanche_average, cache_average]
    p1_data_file.close()
    
def main():
    """
    This is the main() function. 
    It sets up the start of code execution for the script as a program.
    
    Parameters
    ----------
    None

    Returns
    -------
    None
    """
  
    output_file = open('Data_Output.txt', 'w')
        
    for x in range(0,10): # For loop to call and print the max, min, and average functions for the first 10 columns
        col_max=Max_Value(x) 
        col_min=Min_Value(x)
        col_average=Average(x)
        print("Maximum " + COLUMNS[x] + " = {}".format(col_max), file=output_file)
        print("Minimum " + COLUMNS[x] + " = {}".format(col_min), file=output_file)
        print("Average " + COLUMNS[x] + " = {}\r\n".format(col_average), file=output_file)
    
    for x in range(0,10): # For loop to call and print max, min, and average functions for the wilderness areas
        wilderness_col_max=Wilderness_Max(x)
        wilderness_col_min=Wilderness_Min(x)
        wilderness_col_avg=Wilderness_Average(x)
        print(AREAS[1],f'Maximum {COLUMNS[x]} = {wilderness_col_max[0]}','\r\n',AREAS[2],f'Maximum {COLUMNS[x]} = {wilderness_col_max[1]}','\r\n',AREAS[3],f'Maximum {COLUMNS[x]} = {wilderness_col_max[2]}','\r\n',AREAS[4],f'Maximum {COLUMNS[x]} = {wilderness_col_max[3]}','\r\n', file=output_file)
        print(AREAS[1],f'Minimum {COLUMNS[x]} = {wilderness_col_min[0]}','\r\n',AREAS[2],f'Minimum {COLUMNS[x]} = {wilderness_col_min[1]}','\r\n',AREAS[3],f'Minimum {COLUMNS[x]} = {wilderness_col_min[2]}','\r\n',AREAS[4],f'Minimum {COLUMNS[x]} = {wilderness_col_min[3]}','\r\n', file=output_file)
        print(AREAS[1],f'Average {COLUMNS[x]} = {wilderness_col_avg[0]}','\r\n',AREAS[2],f'Average {COLUMNS[x]} = {wilderness_col_avg[1]}','\r\n',AREAS[3],f'Average {COLUMNS[x]} = {wilderness_col_avg[2]}','\r\n',AREAS[4],f'Average {COLUMNS[x]} = {wilderness_col_avg[3]}','\r\n', file=output_file)

if __name__ == "__main__":
    main()