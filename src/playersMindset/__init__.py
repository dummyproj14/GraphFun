from sys import argv
#from .manager import manager as cmd
#from .dataset import default_data

from . import cmd

if __name__ == '__main__':
    cmd.__main__(argv)
    
