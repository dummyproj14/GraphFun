# /usr/bin/python
# author : Bjorn Goriatcheff
# date : 24-01-2022
# 

# Numpy library for matrix handling
import numpy as np
import time
from sys import setrecursionlimit
setrecursionlimit(10**6)


def prepare(mat):
    """
    Create a non-oriented adjacency matrix from oriented adjacency matrix representing an oriented graph
    Return the non-oriented adjacency matrix retaining only bidirectionnal connexions
    Note : the returned matrix is strictly triangular superior 

    Keep only transitions if they are reciprocical :
    - Let Adj(n,n) be the adjacency matrix, OAdj the oriented adjacency matrix
    - Let A_i_j be the transition between i-th vertice to j-th vertice
    - if A_i_j and A_j_i both exist in OAdj (OAdj[i,j] = 1 and OAdj[j,i] = 1) then Adj[i,j] = 1
    - Adj is by definition triangular superior strict
    """

    lower = np.tril(mat, -1) # lower triangle of input matrix
    upper = np.triu(mat, 1)  # upper triangle of input matrix

    t_lower = np.transpose(lower) # convert lower triangle to upper one

    mat = np.logical_and(t_lower, upper) # retain only symmetrical transitions 

    return mat


def validate(mat):
    """
    Validate matrix integrity (not written)
    """
    return True

def nonzero(mat, sparse=False):
    """
    Return the list of nonzero indices
    (optional) if matrix is already in "sparse" mode, return the original structure
    """
    if sparse: return mat
    return np.nonzero(mat)

def prune_indices(i_list, j_list, id_, chains):
    """
    Prune list of nodes from visited list
    """

    # sort j with unvisited nodes first
    j_list_remainer = set(j_list[id_:])
    i_list_remainer = set(i_list[id_:])

    j_unvisited = j_list_remainer.difference(chains[0])
    i_unvisited = i_list_remainer.difference(chains[0])

    
    all_ids = range(id_, len(i_list))
    ids = [j_ for j_ in j_list if j_ in j_unvisited ]
    ids += [i_ for i_ in i_list if i_ in i_unvisited ]

    ids = list(set(ids)) # remove duplicated

    j_new = [j_list[newid] for newid in ids]
    i_new = [i_list[newid] for newid in ids]
 
    # override list
    i_list[id_:] = i_new
    j_list[id_:] = j_new

    return (i_list, j_list)

def search_chains(nonzero_indexes, matlen):
    """
    REFACTOR THIS
    """
    chains = []
    start = time.time()
    #print(len(nonzero_indexes[0]), 'non zero indexes to analyse')

    if len(nonzero_indexes[0]) == 0: return []
    i_list, j_list = nonzero_indexes #unpack

    i_list = list(i_list)
    j_list = list(j_list)

    i_head = i_list[0]
    j_head = j_list[0]
    chain = set([i_head, j_head]) # first element, first chain [e.g. :  (0,4)]
    chains.append(chain)

    mem = {i_head: 0, j_head: 0} # both i_head and j_head in initial chain
    id_ = 1
    while id_ < len(i_list):
        i = i_list[id_]
        j = j_list[id_]
        id_ += 1

        # get existing chain id
        id_chain = mem.get(i, -1)

        # create new chain if id is not in existing chain list
        if id_chain < 0 : 

            # new chain structure
            chain = set([i,j])

            # keep in memory for fast chain id access
            mem[i] = len(chains)
            mem[j] = len(chains)
            
            # append new chain to chain list
            chains.append(chain)

        else : 
            # access chain id
            chain = chains[id_chain]
             
            # add new node to chain
            chain.update({j})

            # update memory for fast chain id access
            mem[j] = id_chain


        # periodic check
        # merging existing chains to converge sooner 
        if len(chains) > 2  and (id_ % 10000 == 0): 

            chains = merge_chains(chains)
            # reset mem (chains have changed)
            mem = {}
            for id_chain, chain in enumerate(chains) :
                for elem in chain: mem[i] = id_chain

      
        elif id_ % 10000 == 0 :
            
            # early stopping condition : chain size is max
            if len(chains[0]) == matlen : 
                break

            # prune visited nodes from lists
            #(DISABLED)
            i_list, j_list = prune_indices(i_list, j_list, id_, chains) 

    # final merge
    if len(chains) > 1:
        chains = merge_chains(chains)

    # end timer for chain search
    t_end_valid = time.time() - start
    
    return chains


def merge_chains(chains):
    """
    Merge multiple chains of linked indices whenever possible (intersection between chains not empty)
    Return the list of merged chains
    (recursive function) 
    """
    merged = []
    if len(chains) < 1 : return []
    if len(chains) < 2 : return [chains[0]]
    if len(chains) == 2 : 
       if not chains[0].isdisjoint(chains[1]) : 
           chains[0].update(chains[1])
           return [chains[0]] #accumulate results
       return chains
    head = chains[0]

    # lookup for chains that can are not disjoint with head chain
    joint = [ chain for chain in chains[1:] if not chain.isdisjoint(head)]
   
    # filter remaining chains
    chains = [chain for chain in chains[1:] if chain not in joint] # remove mergable

    # merge head with non disjoint chains
    for chain in joint:
        head.update(chain)
   
    # return merged head and attempt to merge the rest
    return [head]+merge_chains(chains)
    

def search(mat, debug=False):
    """ 
    Search for the size of the longest chain of linked indices in the adjacency matrix
    Return an integer representing the size of the longest chain
    """
    if debug: import pdb; pdb.set_trace()

    # prepare matrix (remove non-symmetrical connexion)
    mat = prepare(mat)

    # check for dense matrix
    #(dense, null_ids) = isdensediag(mat)
    #if dense :
    

    # get list of nonzero indices
    indices = nonzero(mat)
    #print(f'nonzero {len(indices)}')
    
    # initialize timer
    start = time.time()

    # compute chain list of linked indices (representing connex subgraphs)
    chains = search_chains(indices, len(mat))

    # end timer for chain search
    t_end_chain = time.time() - start

    # return early if no chain found
    if len(chains) == 0 : return 0

    if len(chains) > 1 : 

        # final merge non disjoints chains (common indice)
        chains = merge_chains(chains)

    # stop timer for merging 
    t_end_merge = time.time() - t_end_chain - start

    # display timing (TODO: move to logging)
    #print('timing:')
    #print(f'chains : {t_end_chain}')
    #print(f'merge : {t_end_merge}')
    
    # (DEBUG) print size of longest chain
    # print(sorted(list(max(chains))))
    
    return len(max(chains))


def isdensediag(mat):
    """
    Verify the density of the diagonal indices (above first diagonal)
    Return a boolean set to True if the diagonal is almost positive, False otherwise
    Return a list of null indices if densediag
    """
    # get matrix size
    size = len(mat)
    # extract diagonal
    diag = mat.diagonal(1)
    # get null indices ratio
    null_ids = np.nonzero(diag)[0]
    if len(null_ids) < 0.1 * size: 
        return (True, null_ids) 
    return (False, [])

