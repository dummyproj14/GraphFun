# program controller
from sys import argv, exit

from .textparser import dataset
from .dataset import transform
from .search import search

def manager(inputtext):
    """
    Controller for data flow and modules dependencies
    
    """


    # extract and verify dataset
    data = dataset(inputtext)
    # transform into matrix 
    data = transform(data)
    # search for longest chain of accessible entries
    result = search(data)

    print(result)

if __name__ == '__main__':
    print(argv)
    if len(argv) < 2 :
        print('Please provide a path to a text file containing the target data')
        exit(-1)
    manager(argv[1])
        
    
