"""
This file contains the D06_Exercise3 program. 
Program is designed to output the key and value pairs for a dictionary. 

Author: Jonah Hart

Default Command-Line Usage:
    
    python DO6_Exercise3.py file_name
    
"""

article_file=open("./data/article.bib", encoding="UTF-8")

def get_next_line(file):
    """
    This function opens the file and seperates the keys from their respective values in the dictionary.
    
    Parameters
    ----------
    file : text file
        a text file that contains a dictionary
        
    Returns
    -------
    split_file
        a list with the key and value of that line. 
    """
    
    split_file = file.readline().strip(",\n").split(" = ")
    return split_file

# Reading first line of file in
line1=article_file.readline()

# Calling the get_next_line() function and unpacking the returns into the variables key and value
key1, value1 = get_next_line(article_file)
key2, value2 = get_next_line(article_file)
key3, value3 = get_next_line(article_file)
key4, value4 = get_next_line(article_file)
key5, value5 = get_next_line(article_file)
key6, value6 = get_next_line(article_file)
key7, value7 = get_next_line(article_file)
key8, value8 = get_next_line(article_file)
key9, value9 = get_next_line(article_file)

# Printing the key value pairs
print([key1, value1],[key2, value2],[key3, value3],[key4, value4],[key5, value5],[key6, value6],[key7, value7],[key8, value8],[key9, value9])

article_file.close()