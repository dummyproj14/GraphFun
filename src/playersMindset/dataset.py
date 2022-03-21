# /usr/bin/python
# author : Bjorn Goriatcheff
# date : 23-01-2020
# description : Data transformation and synthetic data generation (random sampler)

# libraries
import numpy as np
from math import sqrt
from random import randint, choices, shuffle # needed to generate tables

# internal modules
from .textparser import read_data
#from .data import default_data


MAX_DEFAULT_DIM = 64 # default vector dimension for matrix generation of shape (8,8)


def transform(dataset):
    """
    Transform a dictionnary based dataset representing a graph
    Into an adjacency matrix representing the connexions of the given graph
    """

    keys = list(set(dataset.keys()))
    values = list(dataset.values())
    # concatenate values into a single list
    all_values = []
    for val in values : all_values.extend(val)
    all_values = list(set(all_values))

    # cardinal of elements in dataset
    all_entries = set(keys+all_values)
    dim = len(all_entries) # matrix dimension (1 row per uniq datapoint) 

    name_2_int = { name : i for i, name in enumerate(all_entries)}

    # TODO : check for sparcity/density when dim > 10**8  
    
    matrix = np.zeros((dim, dim), dtype='B')

    # fill matrix with entries
    for key in keys:
        values = dataset[key]
        key = name_2_int[key]
        for v in values:
            v = name_2_int[v]
            matrix[key,v] = 1
 
    return matrix


def sampling(n=-1, mode=0, prob=0.1):
    """
    Sampling random inputs for testing purposes (finite computing time complexity)
    3 different modes are available (sparse, dense, random) for flexible distribution generation
    Probability is optional
    Return a 2D numpy array
    """

    if n < 0 : 
        n = randint(1, MAX_DEFAULT_DIM)

    if mode == 0:
        flat = sparse_dist(n, prob)
    elif mode == 1:
        flat = dense_dist(n, prob)
    else : 
        flat = np.random.randint(0, 2, n) 

    # take the nearst integer if input size is not a square
    s_root = int(sqrt(n))

    # reshape vector into a 2D matrix
    mat = flat.reshape((s_root, s_root))

    # remove any diagonal
    mat = np.tril(mat, -1) + np.triu(mat, 1)
   
    return mat


def sparse_dist(size, prob=0.03):
    """
    Sparse vector generator : generate a sparse distribution of {1} in the space {0, 1} following a bernoulli law of n=size
    Max 3% of {1} indices (default)
    Return a 1D numpy array
    """

    # large sparse matrix M, shape(M) > (10000, 10000)
    # this is a special case for big data purposes    

    if size > (10 ** 9) :
        # split into sub distributions (for very large sizes)
        dist = [sparse_dist(size//10, prob=prob)]
        for _ in range(9):
            dist += [sparse_dist(size//10, prob=prob)]
        # merge
        dist = np.hstack(dist) 

    # small and medium matrix M, shape(M) < (10000, 10000) 
    # instant generation 
    else: 
        # cast vector as numpy 'B' dtype to save memory
        # only few bytes are needed per elem
        dist = np.random.binomial(1, prob, size).astype('B')

    # verify distribution

    return dist
        
def dense_dist(size, prob=0.03):
    """
    Dense vector generator : generate a dense distribution of {1} in the space {0, 1} following a bernoulli law of n=size
    Dense distribution of positive indices (97%)
    Max 3% of {0} (default)
    Return a 1D numpy array
    """
    if size > 10 ** 9 :
        # split into sub distributions (for very large sizes)
        dist = [dense_dist(size//10, prob=prob)]
        for _ in range(9):
            dist += [dense_dist(size//10, prob=prob)]
        # merge
        dist = np.hstack(dist) 
        return dist

    # draw samples from binomial law
    dist = np.random.binomial(1, 1-prob, size).astype('B')

    return dist


