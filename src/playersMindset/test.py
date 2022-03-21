# # # # # # # # # # # # # # # # #
#
# /usr/bin/python
# author : Bjorn Goriatcheff
# date : 24-01-2022
# name : test.py
# description : testing module for graph search (size of longest connex subgraph
# reduced to its set vertices
#  
#
# # # # # # # # # # # # # # # # #

#import pytest
import numpy as np
from numpy import array, uint8
from random import randint, choices

from .search import search

def test_zero():
    print('testing for 0 as target output')
    sizes = [(i,i) for i in range(1, 50)]
    for id_size, size in enumerate(sizes):
        M = np.zeros(size)
        assert search(M)==0, f"[test_zero] Failing unit test with size {size}, expecting 0"

def test_zero_2():
    print('testing for 0 as target output (2)')
    sizes = [(i,i) for i in range(2, 50)]
    for id_size, size in enumerate(sizes):
        M = np.zeros(size)
        i,j = randint(0, size[0]-1), randint(0, size[0]-1)
        M[i,j] = 1 
        assert search(M)==0, f"[test_zero_2] Failing unit test with size {size}, expecting 0"

def test_zero_3():
    print('testing for 0 as target output (3)')
    # single entry test 
    
    M = np.array([[1]])
    assert search(M) == 0, f"[test_zero_3] Failing unit test with size 1, expecting 0 as output"

    # 2 entries tests
    M = np.array([[1,0],[1,1]])
    assert search(M) == 0, f"[test_zero_3] Failing unit test with size 2, expecting 0 as output"
    
    M = np.array([[1,1],[0,1]])
    assert search(M) == 0, f"[test_zero_3] Failing unit test with size 2, expecting 0 as output"

    # diagonal input (random size)

    i = randint(2, 100)
    M = np.eye(i,i) # ixi
    assert search(M) == 0, f"[test_zero_3] Failing unit test with size {i}, expecting 0 as output"

def test_zero_4():
    print('testing for 0 as target output (4)')
    n = randint(3, 100)
    i = randint(0, n-1)
    
    M = np.zeros((n,n))
    M[i,i] = 1
    M[i,i] = 1
    assert search(M) == 0, f"[test_zero_4] Failing unit test with size {i}, expecting 0 as output"


    # non random
    M = array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=uint8)
   
    assert search(M) == 0, f"[test_zero_4] Failing unit test with size {i}, expecting 0 as output"

def test_two():
    print('testing for 2 as target output')
    n = randint(3, 100)
    i = randint(0, n-1)
    p = randint(0, n-1)

    if i == p : return test_two() # redraw
    
    M = np.zeros((n,n))
    M[i,p] = 1
    M[p,i] = 1
    assert search(M) == 2, f"[test_zero_3] Failing unit test with size {i}, expecting 2 as output"

    M = array([[0, 1],
               [1, 0]], dtype=uint8)

    assert search(M) == 2, f"[test_zero_3] Failing unit test with input {M}, expecting 2 as output"

def test_medium():
    """
    Simple chain above principale diagonal
    """
    M = array([[0, 1, 0, 1],
               [0, 0, 0, 1],
               [1, 1, 0, 1],
               [0, 1, 1, 0]])

    assert search(M) == 3, f"[test_medium] Failing unit test with medium size {M} expecting 3 as output"

    M = array([[0, 0, 1, 1],
               [0, 0, 1, 1],
               [0, 1, 0, 1],
               [1, 1, 1, 0]])


    assert search(M) == 4, f"[test_medium] Failing unit test with medium size {M} expecting 4 as output"

    M = array([[0, 0, 0, 0, 0],
               [0, 0, 1, 0, 1],
               [0, 1, 0, 1, 0],
               [1, 0, 1, 0, 1],
               [0, 1, 1, 0, 0]])

    assert search(M) == 4, f"[test_medium] Failing unit test with medium size {M} expecting 4 as output"

    M = array([[0, 1, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 1, 0]])

    result = search(M) 
    assert result == 3, f"[test_medium] Failing unit test with medium size {M} expecting 3 as output got {result}"


def test_medium_2():
    """

    """
    M = array([[0, 1, 1, 1, 1, 1],
               [1, 0, 1, 1, 1, 0],
               [0, 0, 0, 1, 1, 1],
               [1, 1, 1, 0, 1, 0],
               [1, 1, 1, 1, 0, 1],
               [1, 1, 1, 1, 1, 0]], 
               dtype=uint8)


    assert search(M) == 6, f"[test_medium] Failing unit test with medium size {M} expecting 6 as output"

    M = array([[0, 0, 0, 1, 1, 0, 1],
               [1, 0, 1, 1, 1, 1, 0],
               [0, 1, 0, 1, 1, 1, 1],
               [0, 1, 1, 0, 0, 1, 1],
               [1, 0, 1, 1, 0, 1, 1],
               [0, 1, 0, 1, 1, 0, 1],
               [0, 1, 0, 1, 0, 1, 0]], dtype=uint8)

  
    assert search(M) == 7, f"[test_medium] Failing unit test with medium size {M} expecting 7 as output"
    
    M = array([[0, 1, 0, 0, 1, 1, 0, 1, 1],
       [1, 0, 0, 1, 1, 1, 0, 1, 0],
       [0, 0, 0, 1, 1, 1, 1, 1, 0],
       [0, 0, 0, 0, 0, 1, 0, 1, 1],
       [1, 0, 0, 1, 0, 0, 0, 1, 1],
       [1, 1, 1, 0, 0, 0, 1, 1, 1],
       [0, 1, 1, 1, 1, 1, 0, 1, 1],
       [1, 1, 1, 0, 1, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 0]], dtype=uint8)

    assert search(M) == 9, f"[test_medium] Failing unit test with medium size {M} expecting 9 as output"

    M = array([[0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
               [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
               [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
               [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1],
               [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
               [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
               [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
               [0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
               [0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0]], 
               dtype=uint8)
 
    assert search(M) == 12, f"[test_medium] Failing unit test with medium size {M} expecting 12 as output"


def test_medium_3():
    """
    Random chain of non zero index [[a,b], [b,c], [c,d], [d,e]...]
    """
    size = 100
   
    
    space = range(0, size)
    n = randint(2, size)
    len_ids = size//10
    N = choices(space, k=len_ids)

    #[[X_0, Y_0], [Y_0, X_1], [X_1, Y_1], [Y_1, X_2],  ... , [X_n, Y_n]]
    M_ids = [[],[]] 
    id_ = 0
    for x,y in zip(N[:-1], N[1:]):
        M_ids[0].append(x)
        M_ids[1].append(y)

    M = np.zeros((size,size))
    M_ids[0] = np.array(M_ids[0])
    M_ids[1] = np.array(M_ids[1])
    M[M_ids] = 1
    tmp = M_ids[0]
    M_ids[0] = M_ids[1]
    M_ids[1] = tmp
    
    # transposition
    M[M_ids] = 1


    result = search(M)

    assert result == len_ids-1, f"[test_medium] Failing unit test with medium size {M} expecting {len_ids-1}  as output got {result}"    

def test_large_sparse():
    """
    Sparse matrix test
    """

    # 10**6 entries , 1% positive

    #M = load_sample('sparse_pow_10_6_1pr.npy')
    #assert search(M)==2


def test_large_dense():
    """
    Dense matrix test
    """


def all_tests():
    print('begin tests')

    # simple cases with output in [0, 2] with small matrix size
    # adding randomization for some cases 
    test_zero()
    test_zero_2()
    test_zero_3()
    test_zero_4()
    test_two()

    # simple cases with output in [2, 100] with medium matrix size
    print('testing medium cases')
    test_medium()
    test_medium_2()
    #BROKENtest_medium_3()

    # large matrix test (sparse)
    test_large_sparse()


    # large matrix test (dense)
    test_large_dense()


    print('end tests')





if __name__ == '__main__':
     all_tests()
