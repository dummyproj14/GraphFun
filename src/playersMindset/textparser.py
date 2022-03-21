# /usr/bin/python
# author : Bjorn Goriatcheff
# date : 24-01-2022
# name : textparser.py

from os.path import exists as pth_exists
from os.path import dirname #remove

# Exceptions


current_directory = dirname(__file__)

def read_data(filepath):
    data = []

    # Path verification
    if not pth_exists(filepath):
        raise FileNotFoundError(f"Invalid path provided : {filepath}, please make sure you provided a valid path")

    # Open file at given path
    with open(filepath) as f:
        data = f.readlines()

    # Remove 'end-of-line' char for each line
    data = [line.strip('\n') for line in data]

    return data

def verify_data(data):
    """
    Verify data integrity using provided format
    Expecting 
    """
    # Non-empty content verification
    if len(data) == 0:
        raise ValueError("Empty file provided : {filepath}, please verify the file contents")

    # Format verification
    #verify_data_format(data)
    
    return data

def parse(data):
    """
    Parse dataset information into dictionnary data structure information
    Each dictionnary key represent a 'player' 
    Each dictionnary values represent the list of visible players for a given player
    Return a dictionnary containing the dataset information  
    """

    
    # generate the list of entities per row from raw data
    data = [row.split(',') for row in data]
    
    # generate dataset dictionnary
    # each row has been previously checked for integrity (at least 2 entities per row) 
    dataset = dict([[row[0], row[1:]] for row in data])

    return dataset


def dataset(filepath):
    """
    Dataset parsing wrapper (I/O -> verification -> parsing -> validation) 
    """

    # read input data (I/O from file)
    data = read_data(filepath)

    # verify raw data integrity 
    verify_data(data)
    
    # parse raw data into structured format (dict)
    dataset = parse(data) 
    
    # validate parsed data 
    #validation(dataset)
    
    return dataset





